def test_lien_reservation_affiche_pour_competition_future(client, clubs, competitions):
    reponse = client.post("/showSummary", data={"email": "test@club.com"})
    assert b"/book/Competition%20Future/Club%20Test" in reponse.data


def test_lien_reservation_cache_pour_competition_passee(client, clubs, competitions):
    reponse = client.post("/showSummary", data={"email": "test@club.com"})
    assert b"/book/Competition%20Passee/Club%20Test" not in reponse.data
