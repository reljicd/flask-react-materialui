from flask import Flask

from app.config.env_vars import (POSTGRES_DB, POSTGRES_HOST, POSTGRES_PASSWORD,
                                 POSTGRES_PORT, POSTGRES_USER)
from app.db.database import init_db


def create_app(test_config=None):
    # create and configure the react-app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI=(
            f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@'
            f'{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}')
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    init_db(app)

    from .api import medals
    app.register_blueprint(medals.bp)
    from .api import countries
    app.register_blueprint(countries.bp)

    return app
