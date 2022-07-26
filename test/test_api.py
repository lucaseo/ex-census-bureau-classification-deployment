import json

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


def test_post_below_class():
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
    }

    with TestClient(app) as client:

        data = {"age": 37,
                "workclass": "State-gov",
                "education": "Bachelors",
                "marital-status": "Never-married",
                "occupation": "Adm-clerical",
                "relationship": "Not-in-family",
                "race": "White",
                "sex": "Male",
                "native-country": "United-States",
                "hours-per-week": 40}

        response = client.post("/prediction", headers=headers, data=json.dumps(data))
        assert response.status_code == 200
        assert response.json()['pred_result']['salary'] == '<=50K'


def test_post_above_class():
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
    }

    with TestClient(app) as client:

        data = {"age": 43,
                "workclass": "Private",
                "education": "Some-college",
                "marital-status": "Separated",
                "occupation": "Transport-moving",
                "relationship": "Unmarried",
                "race": "White",
                "sex": "Male",
                "native-country": "United-States",
                "hours-per-week": 51}

        response = client.post("/prediction", headers=headers, data=json.dumps(data))
        assert response.status_code == 200
        assert response.json()['pred_result']['salary'] == '>50K'
