from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from app.database import get_db
from app.model.post import Post
from app.schemas.post import PostCreate, PostOut, PostUpdate
from app.core.oauth2 import get_current_user
from app.core.redis import redis_client
import json

router = APIRouter(prefix="/api/v1/posts", tags=["Posts"])


@router.post("", response_model=PostOut)
async def create_post(
    data: PostCreate, db=Depends(get_db), user=Depends(get_current_user)
):
    post = Post(title=data.title, content=data.content, user_id=user.id)

    db.add(post)
    await db.commit()
    await db.refresh(post)

    await redis_client.delete(f"user:{user.id}:posts")

    return PostOut.model_validate(post)


@router.get("", response_model=list[PostOut])
async def get_my_posts(db=Depends(get_db), user=Depends(get_current_user)):
    cache_key = f"user:{user.id}:posts"

    cached = await redis_client.get(cache_key)
    if cached:
        print("CACHE HIT")
        return json.loads(cached)

    result = await db.execute(select(Post).where(Post.user_id == user.id))
    posts = result.scalars().all()

    serialized = []
    for post in posts:
        d = PostOut.model_validate(post).model_dump()
        d["id"] = str(d["id"])
        serialized.append(d)

    await redis_client.set(cache_key, json.dumps(serialized), ex=60)

    return serialized


@router.get("/{post_id}", response_model=PostOut)
async def get_post(post_id: str, db=Depends(get_db), user=Depends(get_current_user)):
    post = await db.get(Post, post_id)

    if not post or post.user_id != user.id:
        raise HTTPException(403, "Post not found or access denied")

    return PostOut.model_validate(post)


@router.put("/{post_id}", response_model=PostOut)
async def update_post(
    post_id: str, data: PostUpdate, db=Depends(get_db), user=Depends(get_current_user)
):
    post = await db.get(Post, post_id)

    if not post or post.user_id != user.id:
        raise HTTPException(403, "Post not found or access denied")

    if data.title is not None:
        post.title = data.title

    if data.content is not None:
        post.content = data.content

    await db.commit()
    await db.refresh(post)

    await redis_client.delete(f"user:{user.id}:posts")

    return PostOut.model_validate(post)


@router.delete("/{post_id}")
async def delete_post(post_id: str, db=Depends(get_db), user=Depends(get_current_user)):
    post = await db.get(Post, post_id)

    if not post or post.user_id != user.id:
        raise HTTPException(403, "Post not found or access denied")

    await db.delete(post)
    await db.commit()

    await redis_client.delete(f"user:{user.id}:posts")

    return {"message": "Post deleted"}
