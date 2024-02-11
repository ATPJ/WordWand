import pytest

from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture
def client():
    return TestClient(app)


def test_root(client: TestClient):
    res = client.get("/")
    assert res.status_code == 200
