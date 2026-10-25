from server import book_places, get_booked_places, validate_booking


def test_book_places_enregistre_les_places_reservees(clubs, competitions):
    book_places(clubs[2], competitions[0], 3)
    assert get_booked_places(clubs[2], competitions[0]) == 3


def test_validate_booking_cumul_jusqu_a_12_autorise(clubs, competitions):
    book_places(clubs[2], competitions[0], 10)
    assert validate_booking(clubs[2], competitions[0], 2) is None


def test_validate_booking_cumul_au_dela_de_12_refuse(clubs, competitions):
    book_places(clubs[2], competitions[0], 10)
    erreur = validate_booking(clubs[2], competitions[0], 3)
    assert erreur == "Sorry, you cannot book more than 12 places per competition."