from server import app, is_past_competition


def test_is_past_competition_disponible_dans_les_pages():
    with app.test_request_context():
        context = {}
        app.update_template_context(context)
        assert context["is_past_competition"] is is_past_competition