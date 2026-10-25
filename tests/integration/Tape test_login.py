def test_login_email_valide_affiche_le_resume(client, clubs):
    reponse = client.post("/showSummary", data={"email": "test@club.com"})
    assert reponse.status_code == 200
    assert b"Welcome, test@club.com" in reponse.data


def test_login_email_inconnu_affiche_une_erreur(client, clubs):
    reponse = client.post("/showSummary", data={"email": "faux@test.com"})
    assert reponse.status_code == 200
    assert b"Sorry, this email is not registered." in reponse.data


def test_login_email_vide_affiche_une_erreur(client, clubs):
    reponse = client.post("/showSummary", data={"email": ""})
    assert reponse.status_code == 200
    assert b"Sorry, this email is not registered." in reponse.data