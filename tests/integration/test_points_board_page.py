def test_tableau_points_accessible_sans_connexion(client, clubs):
    reponse = client.get("/pointsBoard")
    assert reponse.status_code == 200
    assert b"<td>Club Test</td>" in reponse.data
    assert b"<td>10</td>" in reponse.data


def test_tableau_points_affiche_tous_les_clubs(client, clubs):
    reponse = client.get("/pointsBoard")
    assert b"<td>Petit Club</td>" in reponse.data
    assert b"<td>Grand Club</td>" in reponse.data


def test_tableau_points_mis_a_jour_apres_reservation(client, clubs, competitions):
    client.post("/purchasePlaces", data={
        "club": "Club Test",
        "competition": "Competition Future",
        "places": "3",
    })
    reponse = client.get("/pointsBoard")
    assert b"<td>7</td>" in reponse.data


def test_lien_vers_tableau_points_sur_accueil(client):
    reponse = client.get("/")
    assert b'href="/pointsBoard"' in reponse.data