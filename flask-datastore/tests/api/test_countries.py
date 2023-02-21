def test_by_id(client):
    country_id = 5
    response = client.get(f'/countries/{country_id}')
    assert response.json['id'] == country_id


def test_by_code(client):
    code = 'PER'
    response = client.get(f'/countries/code/{code}')
    assert response.json['code'] == code


COUNTRIES_COUNT = 202


def test_all(client):
    count = 0
    page = 1
    per_page = 100

    response = client.get(f'/countries/all?page={page}&per_page={per_page}')
    count += len(response.json['items'])
    while response.json['has_next']:
        page += 1
        response = client.get(f'/countries/all?page={page}&per_page={per_page}')
        count += len(response.json['items'])

    assert count == COUNTRIES_COUNT
