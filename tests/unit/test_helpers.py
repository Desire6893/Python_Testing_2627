from datetime import datetime, timedelta

from server import (
    booking_confirmation_message,
    find_club_by_email,
    get_points_board,
    is_past_competition,
    parse_places,
)


def competition_a_la_date(date):
    return {"name": "Test", "date": date.strftime("%Y-%m-%d %H:%M:%S"), "numberOfPlaces": "10"}


def test_is_past_competition_hier():
    assert is_past_competition(competition_a_la_date(datetime.now() - timedelta(days=1))) is True


def test_is_past_competition_demain():
    assert is_past_competition(competition_a_la_date(datetime.now() + timedelta(days=1))) is False


def test_parse_places_nombre_negatif():
    assert parse_places("-3") == -3


def test_parse_places_zero():
    assert parse_places("0") == 0


def test_parse_places_avec_espaces():
    assert parse_places(" 4 ") == 4


def test_parse_places_none():
    assert parse_places(None) is None


def test_message_confirmation_douze_places():
    message = booking_confirmation_message(12)
    assert message == "Great-booking complete! You have booked 12 places."


def test_find_club_by_email_sensible_a_la_casse(clubs):
    assert find_club_by_email("TEST@club.com", clubs) is None


def test_points_board_points_en_nombre(clubs):
    assert isinstance(get_points_board(clubs)[0]["points"], int)


def test_points_board_sans_email(clubs):
    assert "email" not in get_points_board(clubs)[0]


def test_points_board_ordre_des_clubs(clubs):
    noms = [ligne["name"] for ligne in get_points_board(clubs)]
    assert noms == ["Club Test", "Petit Club", "Grand Club"]