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

    

def test_achat_refuse_si_12_places_depassees_en_plusieurs_fois(client, clubs, competitions):
    client.post("/purchasePlaces", data={
        "club": "Grand Club",
        "competition": "Competition Future",
        "places": "10",
    })
    reponse = client.post("/purchasePlaces", data={
        "club": "Grand Club",
        "competition": "Competition Future",
        "places": "3",
    })
    assert b"Sorry, you cannot book more than 12 places per competition." in reponse.data
    assert int(clubs[2]["points"]) == 10

    
def test_achat_refuse_si_plus_de_places_que_disponibles(client, clubs, competitions):
    reponse = client.post("/purchasePlaces", data={
        "club": "Club Test",
        "competition": "Petite Competition",
        "places": "3",
    })
    assert reponse.status_code == 200
    assert b"Sorry, there are not enough places left in this competition." in reponse.data
    assert int(clubs[0]["points"]) == 10
    assert int(competitions[2]["numberOfPlaces"]) == 2

    
def test_achat_refuse_si_competition_passee(client, clubs, competitions):
    reponse = client.post("/purchasePlaces", data={
        "club": "Club Test",
        "competition": "Competition Passee",
        "places": "1",
    })
    assert reponse.status_code == 200
    assert b"Sorry, this competition has already taken place." in reponse.data
    assert int(clubs[0]["points"]) == 10
    assert int(competitions[1]["numberOfPlaces"]) == 25

    

def test_achat_refuse_si_places_negatives(client, clubs, competitions):
    reponse = client.post("/purchasePlaces", data={
        "club": "Club Test",
        "competition": "Competition Future",
        "places": "-5",
    })
    assert reponse.status_code == 200
    assert b"Sorry, the number of places must be greater than 0." in reponse.data
    assert int(clubs[0]["points"]) == 10
    assert int(competitions[0]["numberOfPlaces"]) == 20

    

def test_achat_refuse_si_places_en_lettres(client, clubs, competitions):
    reponse = client.post("/purchasePlaces", data={
        "club": "Club Test",
        "competition": "Competition Future",
        "places": "abc",
    })
    assert reponse.status_code == 200
    assert b"Sorry, please enter a valid number of places." in reponse.data
    assert int(clubs[0]["points"]) == 10


def test_achat_refuse_si_places_vide(client, clubs, competitions):
    reponse = client.post("/purchasePlaces", data={
        "club": "Club Test",
        "competition": "Competition Future",
        "places": "",
    })
    assert reponse.status_code == 200
    assert b"Sorry, please enter a valid number of places." in reponse.data
    assert int(clubs[0]["points"]) == 10