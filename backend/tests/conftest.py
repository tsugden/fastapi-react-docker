import pytest
from app.config import Settings, get_settings
from app.db import close_db, init_db
from app.main import create_application
from fastapi.testclient import TestClient


def get_settings_override():
    return Settings(environment="test")


@pytest.fixture(scope="module")
def test_app():
    # set up
    app = create_application()
    app.dependency_overrides[get_settings] = get_settings_override

    with TestClient(app) as test_client:

        # testing
        yield test_client

    # tear down


@pytest.fixture(scope="module")
def test_app_with_db():
    # set up
    app = create_application()
    app.dependency_overrides[get_settings] = get_settings_override
    app.add_event_handler("startup", init_db)
    app.add_event_handler("shutdown", close_db)

    with TestClient(app) as test_client:

        # testing
        yield test_client

    # tear down
