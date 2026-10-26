from server import validate_booking


def test_validate_booking_zero_place_refuse(clubs, competitions):
    erreur = validate_booking(clubs[0], competitions[0], 0)
    assert erreur == "Sorry, the number of places must be greater than 0."


def test_validate_booking_places_negatives_refuse(clubs, competitions):
    erreur = validate_booking(clubs[0], competitions[0], -5)
    assert erreur == "Sorry, the number of places must be greater than 0."


def test_validate_booking_une_place_autorise(clubs, competitions):
    assert validate_booking(clubs[0], competitions[0], 1) is None
