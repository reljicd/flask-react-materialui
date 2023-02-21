def test_years(client):
    response = client.get(f'/medals/years')
    assert len(response.json) == 3


COUNTRIES_WITH_MEDALS = 103


def test_per_countries(client):
    response = client.get(f'/medals/per_country')
    assert len(response.json) == COUNTRIES_WITH_MEDALS


COUNTRIES_WITH_MEDALS_2012 = 85


def test_per_countries_per_year(client):
    year = 2012
    response = client.get(f'/medals/per_country/{year}')
    assert len(response.json) == COUNTRIES_WITH_MEDALS_2012
