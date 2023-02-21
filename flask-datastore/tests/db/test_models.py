from app.db.models import Country, Medal

COUNTRIES_COUNT = 202


def test_countries_count(app):
    with app.app_context():
        assert Country.query.count() == COUNTRIES_COUNT


MEDALS_COUNT = 5989


def test_medals_count(app):
    with app.app_context():
        assert Medal.query.count() == MEDALS_COUNT


def test_medal_country_relation(app):
    with app.app_context():
        assert isinstance(Medal.query.first().country, Country)
