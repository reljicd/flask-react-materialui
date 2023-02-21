def test_by_id(client):
    medal_id = 5
    response = client.get(f'/countries/{medal_id}')
    assert response.json['id'] == medal_id


MEDALS_COUNT = 5989


def test_all(client):
    count = 0
    page = 1
    per_page = 100

    response = client.get(f'/medals/all?page={page}&per_page={per_page}')
    count += len(response.json['items'])
    while response.json['has_next']:
        page += 1
        response = client.get(f'/medals/all?page={page}&per_page={per_page}')
        count += len(response.json['items'])

    assert count == MEDALS_COUNT


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
