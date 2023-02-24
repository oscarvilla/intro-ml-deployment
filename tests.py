from fastapi.testclient import TestClient

from api.main import app

cliente = TestClient(app)


def test_null_prediction():
    response = cliente.post("/v1/prediction", json={
        "opening_gross": 0,
        "screens": 0,
        "production_budget": 0,
        "title_year": 0,
        "aspect_ratio": 0,
        "duration": 0,
        "cast_total_facebook_likes": 0,
        "budget": 0,
        "imdb_score": 0
    })
    assert response.status_code == 200
    assert response.json()["worldwide_gross"] == 0


def test_random_prediction():
    response = cliente.post("/v1/prediction", json={
        "opening_gross": 8330681,
        "screens": 2271,
        "production_budget": 13000000,
        "title_year": 1999,
        "aspect_ratio": 1.85,
        "duration": 97,
        "cast_total_facebook_likes": 37907,
        "budget": 16000000,
        "imdb_score": 7.2
    })

    assert response.status_code == 200
    assert response.json()["worldwide_gross"] != 0
