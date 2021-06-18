def test_ping(test_app_with_db):
    response = test_app_with_db.get("/ping")
    assert response.status_code == 200
    assert response.json() == {
        "environment": "test",
        "ping": "pong",
        "db_name": "fastapi-react-docker",
        "projects": {
            "_id": "706e08bf-b275-404a-8bf3-29a749c208a0",
            "name": "dean",
            "nickname": "nickname",
        },
    }
