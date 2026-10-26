from server import book_places


def test_book_places_deduit_les_points_du_club(clubs, competitions):
    book_places(clubs[0], competitions[0], 3)
    assert int(clubs[0]["points"]) == 7


def test_book_places_deduit_les_places_de_la_competition(clubs, competitions):
    book_places(clubs[0], competitions[0], 3)
    assert int(competitions[0]["numberOfPlaces"]) == 17
