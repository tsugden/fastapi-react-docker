import logging
import os
from functools import lru_cache
from typing import Optional

from pydantic import BaseSettings

log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    environment: Optional[str] = os.environ.get("ENVIRONMENT")
    testing: Optional[str] = os.environ.get("TESTING")
    db_name: Optional[str] = os.environ.get("MONGO_DATABASE_NAME")


@lru_cache
def get_settings() -> BaseSettings:
    log.info("Loading config settings from the environment...")
    return Settings()
