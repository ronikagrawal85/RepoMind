from fastapi import FastAPI

from app.api.router import api_router

app = FastAPI(
    title="RepoMind API",
    description="Backend API for RepoMind",
    version="0.1.0",
)

app.include_router(api_router)
