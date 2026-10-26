import os

import pytest

PAGES = ["index.html", "welcome.html", "booking.html", "points_board.html"]


@pytest.mark.parametrize("page", PAGES)
def test_page_html_bien_fermee(page):
    with open(os.path.join("templates", page), encoding="utf-8") as fichier:
        contenu = fichier.read()
    assert contenu.strip().endswith("</html>")