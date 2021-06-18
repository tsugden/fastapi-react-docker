import logging

from motor.motor_asyncio import AsyncIOMotorClient

# import os


log = logging.getLogger("uvicorn")


class Database:
    client: AsyncIOMotorClient


db = Database()


def get_database():
    return db.client


def init_db():
    log.info("Connecting to database...")
    """
    db.client = AsyncIOMotorClient(
        os.environ.get("MONGO_DATABASE_HOST"),
        username=os.environ.get("MONGO_DATABASE_USERNAME"),
        password=os.environ.get("MONGO_DATABASE_PASSWORD"),
        authSource=os.environ.get("MONGO_DATABASE_NAME"),
    )
    """
    db.client = AsyncIOMotorClient(
        "mongodb://tomuser:tompass@db:27017/?authSource=fastapi-react-docker"
    )
    log.info("Connected")


def close_db():
    log.info("Closing database...")
    db.client.close()
