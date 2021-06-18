from app.config import Settings, get_settings
from app.db import Database, get_database
from fastapi import APIRouter, Depends

router = APIRouter()


@router.get("/ping")
async def pong(
    settings: Settings = Depends(get_settings),
    database: Database = Depends(get_database),
):
    projects = await database[settings.db_name]["projects"].find_one()

    return {
        "ping": "pong",
        "environment": settings.environment,
        "db_name": settings.db_name,
        "projects": projects,
    }
