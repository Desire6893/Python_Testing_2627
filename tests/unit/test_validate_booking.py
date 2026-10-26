from server import validate_booking


def test_validate_booking_assez_de_points(clubs, competitions):
    assert validate_booking(clubs[0], competitions[0], 3) is None


def test_validate_booking_tous_ses_points(clubs, competitions):
    assert validate_booking(clubs[0], competitions[0], 10) is None


def test_validate_booking_pas_assez_de_points(clubs, competitions):
    erreur = validate_booking(clubs[1], competitions[0], 5)
    assert erreur == "Sorry, you do not have enough points."

    

def test_validate_booking_12_places_autorise(clubs, competitions):
    assert validate_booking(clubs[2], competitions[0], 12) is None


def test_validate_booking_plus_de_12_places_refuse(clubs, competitions):
    erreur = validate_booking(clubs[2], competitions[0], 13)
    assert erreur == "Sorry, you cannot book more than 12 places per competition."

    

def test_validate_booking_toutes_les_places_restantes(clubs, competitions):
    assert validate_booking(clubs[0], competitions[2], 2) is None


def test_validate_booking_plus_de_places_que_disponibles(clubs, competitions):
    erreur = validate_booking(clubs[0], competitions[2], 3)
    assert erreur == "Sorry, there are not enough places left in this competition."