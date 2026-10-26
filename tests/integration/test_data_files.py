from server import is_past_competition, loadClubs, loadCompetitions


def test_le_fichier_contient_au_moins_une_competition_a_venir():
    competitions = loadCompetitions()
    assert any(not is_past_competition(c) for c in competitions)


def test_le_fichier_contient_des_clubs():
    assert len(loadClubs()) > 0
