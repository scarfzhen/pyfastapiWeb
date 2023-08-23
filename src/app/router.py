from fastapi import APIRouter, BackgroundTasks
from pydantic import UUID4

router = APIRouter()


@router.get("/ping")
async def ping():
    """send pong to user"""
    return {"status": "ok"}
