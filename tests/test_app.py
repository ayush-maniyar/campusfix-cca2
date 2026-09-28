from app import app


def test_home_page():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200


def test_health_endpoint():
    client = app.test_client()
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json["status"] == "ok"


def test_add_complaint():
    client = app.test_client()

    response = client.post(
        "/complaint",
        data={
            "name": "Ayush",
            "room": "A-101",
            "category": "Electrical",
            "description": "Fan is not working"
        }
    )

    assert response.status_code == 302
