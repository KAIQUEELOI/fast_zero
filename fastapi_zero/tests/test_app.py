
from fastapi.testclient import TestClient

from fastapi_zero.app import app

client = TestClient(app)


def test_root_deve_retornar_ola_mundo():
    response = client.get("/")

    assert response.status_code == 200
    assert response.text == "<h1>Olá mundo!</h1>"
    assert response.headers["content-type"] == "text/html; charset=utf-8"
