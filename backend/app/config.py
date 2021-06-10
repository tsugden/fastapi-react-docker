import logging
import os
from functools import lru_cache

from pydantic import BaseSettings

log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    ENVIRONMENT: str = os.getenv("ENVIRONMENT")
    TESTING: str = os.getenv("TESTING")
    MONGO_DATABASE: str = os.getenv("MONGO_DATABASE")
    MONGO_USER_USERNAME: str = os.getenv("MONGO_USER_USERNAME")
    MONGO_USER_PASSWORD: str = os.getenv("MONGO_USER_PASSWORD")


@lru_cache()
async def get_settings() -> BaseSettings:
    log.info("Loading config settings from the environment...")
    return Settings()
