from server import get_points_board


def test_points_board_contient_tous_les_clubs(clubs):
    assert len(get_points_board(clubs)) == 3


def test_points_board_nom_et_points(clubs):
    board = get_points_board(clubs)
    assert board[0] == {"name": "Club Test", "points": 10}


def test_points_board_liste_vide():
    assert get_points_board([]) == []