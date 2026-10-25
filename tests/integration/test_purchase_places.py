def test_achat_deduit_les_points_du_club(client, clubs, competitions):
    reponse = client.post("/purchasePlaces", data={
        "club": "Club Test",
        "competition": "Competition Future",
        "places": "3",
    })
    assert reponse.status_code == 200
    assert b"Great-booking complete!" in reponse.data
    assert b"Points available: 7" in reponse.data


def test_achat_refuse_si_pas_assez_de_points(client, clubs, competitions):
    reponse = client.post("/purchasePlaces", data={
        "club": "Petit Club",
        "competition": "Competition Future",
        "places": "5",
    })
    assert reponse.status_code == 200
    assert b"Sorry, you do not have enough points." in reponse.data
    # rien n'a été retiré :
    assert int(clubs[1]["points"]) == 4
    assert int(competitions[0]["numberOfPlaces"]) == 20