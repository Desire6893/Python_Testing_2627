from server import is_past_competition, validate_booking


def test_is_past_competition_date_passee(competitions):
    assert is_past_competition(competitions[1]) is True


def test_is_past_competition_date_future(competitions):
    assert is_past_competition(competitions[0]) is False


def test_validate_booking_competition_passee_refuse(clubs, competitions):
    erreur = validate_booking(clubs[0], competitions[1], 1)
    assert erreur == "Sorry, this competition has already taken place."
