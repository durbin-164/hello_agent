from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_welcome():
    response = client.post("/welcome", json={"name": "A Name"})
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome A Name"}

def test_fail():
    assert 1 == 1