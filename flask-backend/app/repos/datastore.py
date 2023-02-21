from typing import Dict, List

import requests

from app.config.env_vars import DATASTORE_HOST, DATASTORE_PORT

DATASTORE_URL = f'http://{DATASTORE_HOST}:{DATASTORE_PORT}'


class DataStoreRepo(object):

    @staticmethod
    def years() -> List[int]:
        r = requests.get(f'{DATASTORE_URL}/medals/years')
        return r.json()

    @staticmethod
    def medals_per_countries() -> List[Dict]:
        r = requests.get(f'{DATASTORE_URL}/medals/per_country')
        return r.json()

    @staticmethod
    def medals_per_countries_per_year(year: int) -> List[Dict]:
        r = requests.get(f'{DATASTORE_URL}/medals/per_country/{year}')
        return r.json()
