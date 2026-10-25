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
    assert int(clubs[1]["points"]) == 4
    assert int(competitions[0]["numberOfPlaces"]) == 20

    

def test_achat_refuse_si_plus_de_12_places(client, clubs, competitions):
    reponse = client.post("/purchasePlaces", data={
        "club": "Grand Club",
        "competition": "Competition Future",
        "places": "13",
    })
    assert reponse.status_code == 200
    assert b"Sorry, you cannot book more than 12 places per competition." in reponse.data
    assert int(clubs[2]["points"]) == 20
    assert int(competitions[0]["numberOfPlaces"]) == 20