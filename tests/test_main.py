from fastapi.testclient import TestClient
from app.main import app 

client = TestClient(app)


def test_send():
    response = client.post("/send",json={"message": "Hello there"})
    assert response.status_code == 201
    assert response.json() == {"message": "Hello there"}
