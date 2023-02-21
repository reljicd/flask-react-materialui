import os

DATASTORE_HOST: str = os.getenv(key='DATASTORE_HOST', default='localhost')
DATASTORE_PORT: int = int(os.getenv(key='DATASTORE_PORT', default='5001'))
