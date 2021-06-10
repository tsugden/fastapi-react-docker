from fastapi import Depends, FastAPI

from app.config import Settings, get_settings

app = FastAPI()


@app.get("/ping")
def pong(settings: Settings = Depends(get_settings)):
    return {
        "ping": "pong",
        "environment": settings.ENVIRONMENT,
        "testing": settings.TESTING,
        "database": settings.MONGO_DATABASE,
    }
