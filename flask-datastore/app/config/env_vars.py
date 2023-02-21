import os

POSTGRES_HOST: str = os.getenv(key='POSTGRES_HOST', default='localhost')
POSTGRES_PORT: int = int(os.getenv(key='POSTGRES_PORT', default='5432'))
POSTGRES_DB: str = os.getenv(key='POSTGRES_DB', default='flask_react')
POSTGRES_USER: str = os.getenv(key='POSTGRES_USER', default='username')
POSTGRES_PASSWORD: str = os.getenv(key='POSTGRES_PASSWORD', default='password')
