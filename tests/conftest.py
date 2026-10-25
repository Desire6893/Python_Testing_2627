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
        {"name": "Grand Club", "email": "grand@club.com", "points": "20"},
    ]
    monkeypatch.setattr(server, "clubs", test_clubs)
    return test_clubs


@pytest.fixture
def competitions(monkeypatch):
    test_competitions = [
        {"name": "Competition Future", "date": "2030-06-01 10:00:00", "numberOfPlaces": "20"},
        {"name": "Competition Passee", "date": "2020-03-27 10:00:00", "numberOfPlaces": "25"},
        {"name": "Petite Competition", "date": "2030-07-01 10:00:00", "numberOfPlaces": "2"},
    ]
    monkeypatch.setattr(server, "competitions", test_competitions)
    return test_competitions


@pytest.fixture(autouse=True)
def bookings(monkeypatch):
    test_bookings = {}
    monkeypatch.setattr(server, "bookings", test_bookings, raising=False)
    return test_bookings