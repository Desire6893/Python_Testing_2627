from server import find_by_name


def test_find_by_name_trouve_le_club(clubs):
    assert find_by_name(clubs, "Club Test")["email"] == "test@club.com"


def test_find_by_name_trouve_la_competition(competitions):
    assert find_by_name(competitions, "Competition Future")["numberOfPlaces"] == "20"


def test_find_by_name_inconnu_retourne_none(clubs):
    assert find_by_name(clubs, "Club Inconnu") is None