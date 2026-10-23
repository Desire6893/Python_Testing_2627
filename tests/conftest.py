import pytest
import server


@pytest.fixture
def client():
    server.app.config["TESTING"] = True
    with server.app.test_client() as client:
        yield client


@pytest.fixture
def clubs(monkeypatch):
    test_clubs = [
        {"name": "Club Test", "email": "test@club.com", "points": "10"},
        {"name": "Petit Club", "email": "petit@club.com", "points": "4"},
    ]
    monkeypatch.setattr(server, "clubs", test_clubs)
    return test_clubs