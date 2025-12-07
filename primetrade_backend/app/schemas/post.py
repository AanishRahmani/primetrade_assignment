from typing import Optional
from pydantic import BaseModel, Field
import uuid


class PostCreate(BaseModel):
    title: str = Field(
        ...,
        min_length=1,
        max_length=200,
        description="Title of the post",
        examples=["My First Blog Post"]
    )
    content: str | None = Field(
        None,
        max_length=10000,
        description="Content/body of the post",
        examples=["This is the content of my blog post..."]
    )


class PostOut(BaseModel):
    id: uuid.UUID = Field(
        ...,
        description="Unique identifier for the post"
    )
    title: str = Field(
        ...,
        description="Title of the post"
    )
    content: str | None = Field(
        None,
        description="Content/body of the post"
    )
    user_id: int = Field(
        ...,
        description="ID of the user who created this post"
    )

    class Config:
        from_attributes = True


class PostUpdate(BaseModel):
    title: Optional[str] = Field(
        None,
        min_length=1,
        max_length=200,
        description="Updated title of the post",
        examples=["Updated Blog Title"]
    )
    content: Optional[str] = Field(
        None,
        max_length=10000,
        description="Updated content/body of the post",
        examples=["This is the updated content..."]
    )

    class Config:
        from_attributes = True
