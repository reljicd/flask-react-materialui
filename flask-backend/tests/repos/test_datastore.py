from app.repos.datastore import DataStoreRepo


def test_medals_years():
    years = DataStoreRepo.years()
    assert 2012 in years


COUNTRIES_WITH_MEDALS = 103


def test_medals_per_countries():
    assert len(DataStoreRepo.medals_per_countries()) == COUNTRIES_WITH_MEDALS


COUNTRIES_WITH_MEDALS_2012 = 85


def test_medals_per_countries_per_year():
    assert len(DataStoreRepo.medals_per_countries_per_year(
        2012)) == COUNTRIES_WITH_MEDALS_2012
