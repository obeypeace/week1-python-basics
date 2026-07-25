# testing the API created
from fastapi.testclient import TestClient
from src.api import app

client = TestClient(app)
def test_predict_returns_valid_response():
    response = client.post("/predict", json={"age": 29, "fare": 100, "pclass": 1})
    assert response.status_code == 200
    data = response.json()
    assert "survived_prediction" in data
    assert data["survived_prediction"] in [0, 1]

def test_predict_rejects_invalid_pclass():
    response = client.post("/predict", json={"age": 29, "fare": 100, "pclass": 99})
    assert response.status_code == 400