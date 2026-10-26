from server import parse_places


def test_parse_places_nombre_valide():
    assert parse_places("3") == 3


def test_parse_places_vide():
    assert parse_places("") is None


def test_parse_places_lettres():
    assert parse_places("abc") is None


def test_parse_places_nombre_a_virgule():
    assert parse_places("2.5") is None