def test_achat_deduit_les_points_du_club(client, clubs, competitions):
    reponse = client.post("/purchasePlaces", data={
        "club": "Club Test",
        "competition": "Competition Future",
        "places": "3",
    })
    assert reponse.status_code == 200
    assert b"Great-booking complete!" in reponse.data
    assert b"Points available: 7" in reponse.data