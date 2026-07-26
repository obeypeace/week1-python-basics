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

def test_predict_no_feature_name_warning(recwarn):
    """Confirms predict doesn't trigger sklearn's feature-name mismatch warning."""
    response = client.post("/predict", json={"age": 29, "fare": 100, "pclass": 1})
    assert response.status_code == 200
    sklearn_warnings = [w for w in recwarn.list if "feature names" in str(w.message)]
    assert len(sklearn_warnings) == 0
# recwarn is another built-in pytest fixture, 
# similar to caplog but for Python warnings instead of log messages — same mechanism, different thing being captured.

def test_predict_rejects_negative_age():
    response = client.post("/predict", json={"age": -5, "fare": 100, "pclass": 1})
    assert response.status_code == 400

def test_predict_rejects_negative_fare():
    response = client.post("/predict", json={"age": 29, "fare": -50, "pclass": 1})
    assert response.status_code == 400

def test_predict_accepts_zero_fare():
    response = client.post("/predict", json={"age": 29, "fare": 0, "pclass": 1})
    assert response.status_code == 200