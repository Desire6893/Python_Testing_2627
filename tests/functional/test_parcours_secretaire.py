def test_parcours_complet_reservation(client, clubs, competitions):
    reponse = client.get("/")
    assert b"Welcome to the GUDLFT Registration Portal!" in reponse.data

    reponse = client.post("/showSummary", data={"email": "test@club.com"})
    assert b"Points available: 10" in reponse.data

    reponse = client.get("/book/Competition%20Future/Club%20Test")
    assert b"How many places?" in reponse.data

    reponse = client.post("/purchasePlaces", data={
        "club": "Club Test",
        "competition": "Competition Future",
        "places": "2",
    })
    assert b"You have booked 2 places." in reponse.data
    assert b"Points available: 8" in reponse.data

    reponse = client.get("/pointsBoard")
    assert b"<td>8</td>" in reponse.data

    reponse = client.get("/logout", follow_redirects=True)
    assert b"Welcome to the GUDLFT Registration Portal!" in reponse.data


def test_parcours_reservation_refusee_puis_acceptee(client, clubs, competitions):
    client.post("/showSummary", data={"email": "petit@club.com"})

    reponse = client.post("/purchasePlaces", data={
        "club": "Petit Club",
        "competition": "Competition Future",
        "places": "5",
    })
    assert b"Sorry, you do not have enough points." in reponse.data

    reponse = client.post("/purchasePlaces", data={
        "club": "Petit Club",
        "competition": "Competition Future",
        "places": "4",
    })
    assert b"You have booked 4 places." in reponse.data
    assert b"Points available: 0" in reponse.data


def test_parcours_visiteur_non_connecte(client, clubs):
    reponse = client.get("/")
    assert b'href="/pointsBoard"' in reponse.data

    reponse = client.get("/pointsBoard")
    assert b"<td>Petit Club</td>" in reponse.data