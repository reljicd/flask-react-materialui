from app.db.repos import MedalRepo

MEDALS_COUNT = 5989


def test_medals_count(app):
    with app.app_context():
        assert MedalRepo.count() == MEDALS_COUNT


def test_all_per_page(app):
    per_page = 10
    with app.app_context():
        assert MedalRepo.all(per_page=10).per_page == per_page


def test_all_page(app):
    page = 10
    with app.app_context():
        assert MedalRepo.all(page=10).page == page


def test_all(app):
    count = 0
    page = 1
    per_page = 100
    with app.app_context():
        paginator = MedalRepo.all(page=page, per_page=per_page)
        count += len(paginator.items)
        while paginator.has_next:
            page += 1
            paginator = MedalRepo.all(page=page, per_page=per_page)
            count += len(paginator.items)
    assert count == MEDALS_COUNT


def test_medals_years(app):
    with app.app_context():
        years = MedalRepo.years()
        assert 2012 in years


COUNTRIES_WITH_MEDALS = 103


def test_medals_per_countries(app):
    with app.app_context():
        assert len(MedalRepo.per_countries()) == COUNTRIES_WITH_MEDALS


COUNTRIES_WITH_MEDALS_2012 = 85


def test_medals_per_countries_per_year(app):
    with app.app_context():
        assert len(MedalRepo.per_countries_per_year(
            2012)) == COUNTRIES_WITH_MEDALS_2012


def test_medals_per_countries_per_year_alt(app):
    with app.app_context():
        assert len(MedalRepo.per_countries_per_year_alt(
            2012)) == COUNTRIES_WITH_MEDALS_2012
