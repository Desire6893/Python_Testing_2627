from server import find_club_by_email


def test_find_club_by_email_retourne_le_club(clubs):
    club = find_club_by_email("test@club.com", clubs)
    assert club["name"] == "Club Test"

def test_find_club_by_email_inconnu_retourne_none(clubs):
    assert find_club_by_email("faux@test.com", clubs) is None

def test_find_club_by_email_vide_retourne_none(clubs):
    assert find_club_by_email("", clubs) is None