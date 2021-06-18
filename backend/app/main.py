import logging

from fastapi import FastAPI

from app.api import ping
from app.db import close_db, init_db

log = logging.getLogger("uvicorn")


def create_application() -> FastAPI:
    application = FastAPI()
    application.include_router(ping.router)
    return application


app = create_application()


@app.on_event("startup")
async def startup_db_client():
    log.info("Starting up...")
    init_db()


@app.on_event("shutdown")
async def shutdown_db_client():
    log.info("Shutting down...")
    close_db()
