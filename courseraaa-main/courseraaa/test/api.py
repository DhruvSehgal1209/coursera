import pytest
from api.app import app

@pytest.fixture
def client():
    with app.test_client() as c:
        yield c

def test_predict(client):
    res = client.post('/predict', json={'features': [1, 2, 3]})
    assert res.status_code == 200
    assert 'prediction' in res.json
