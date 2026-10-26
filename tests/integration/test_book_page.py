def test_page_reservation_affiche_le_formulaire(client, clubs, competitions):
    reponse = client.get("/book/Competition%20Future/Club%20Test")
    assert reponse.status_code == 200
    assert b"How many places?" in reponse.data


def test_page_reservation_club_inconnu(client, clubs, competitions):
    reponse = client.get("/book/Competition%20Future/Club%20Inconnu")
    assert reponse.status_code == 200
    assert b"Something went wrong-please try again" in reponse.data


def test_page_reservation_competition_inconnue(client, clubs, competitions):
    reponse = client.get("/book/Competition%20Inconnue/Club%20Test")
    assert reponse.status_code == 200
    assert b"Something went wrong-please try again" in reponse.data
    