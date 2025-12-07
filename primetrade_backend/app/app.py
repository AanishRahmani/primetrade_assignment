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
    docs_url=None,
    redoc_url=None,
    openapi_url=None,
)
origins = [
    "https://assignment-front.netlify.app",
    "http://localhost:3000",
    "http://localhost:5173",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Primetrade Backend API is running"}


app.include_router(auth.router)
app.include_router(post.router)
app.include_router(health.router)
