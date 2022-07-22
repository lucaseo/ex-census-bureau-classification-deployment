import pytest
from fastapi.testclient import TestClient

from app import app

@pytest.fixture
def client():
    return TestClient(app)

def test_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Welcome to Census ML Inference API"}