from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.routes import auth, post, health
from app.database import init_db

from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


app = FastAPI(
    title="assignment Backend",
    lifespan=lifespan,
    # docs_url=None,
    # redoc_url=None,
    # openapi_url=None,
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)


@app.get("/")
async def root():
    return {"message": "Primetrade Backend API is running"}


app.include_router(auth.router)
app.include_router(post.router)
app.include_router(health.router)
