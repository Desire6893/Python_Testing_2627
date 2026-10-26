from server import book_places, get_booked_places, validate_booking


def test_get_booked_places_zero_par_defaut(clubs, competitions):
    assert get_booked_places(clubs[0], competitions[0]) == 0


def test_get_booked_places_cumule_plusieurs_reservations(clubs, competitions):
    book_places(clubs[2], competitions[0], 3)
    book_places(clubs[2], competitions[0], 4)
    assert get_booked_places(clubs[2], competitions[0]) == 7


def test_get_booked_places_separe_par_competition(clubs, competitions):
    book_places(clubs[0], competitions[0], 3)
    assert get_booked_places(clubs[0], competitions[2]) == 0


def test_get_booked_places_separe_par_club(clubs, competitions):
    book_places(clubs[0], competitions[0], 3)
    assert get_booked_places(clubs[2], competitions[0]) == 0


def test_book_places_deux_fois_deduit_les_points(clubs, competitions):
    book_places(clubs[0], competitions[0], 3)
    book_places(clubs[0], competitions[0], 2)
    assert int(clubs[0]["points"]) == 5


def test_book_places_ne_touche_pas_les_autres_clubs(clubs, competitions):
    book_places(clubs[0], competitions[0], 3)
    assert int(clubs[1]["points"]) == 4


def test_validate_booking_zero_place_prioritaire(clubs, competitions):
    erreur = validate_booking(clubs[0], competitions[1], 0)
    assert erreur == "Sorry, the number of places must be greater than 0."


def test_validate_booking_competition_passee_prioritaire_sur_les_points(clubs, competitions):
    erreur = validate_booking(clubs[1], competitions[1], 5)
    assert erreur == "Sorry, this competition has already taken place."


def test_validate_booking_club_sans_points(competitions):
    club = {"name": "Club Vide", "email": "vide@club.com", "points": "0"}
    erreur = validate_booking(club, competitions[0], 1)
    assert erreur == "Sorry, you do not have enough points."


def test_validate_booking_points_en_nombre(competitions):
    club = {"name": "Club Nombre", "email": "nombre@club.com", "points": 5}
    assert validate_booking(club, competitions[0], 3) is None