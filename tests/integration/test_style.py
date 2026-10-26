def test_feuille_de_style_chargee(client):
    page = client.get("/")
    assert b"/static/style.css" in page.data
    assert client.get("/static/style.css").status_code == 200
