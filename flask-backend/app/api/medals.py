from flask import Blueprint

from app.repos.datastore import DataStoreRepo

bp = Blueprint('medals', __name__, url_prefix='/medals')


@bp.route('/years')
def years():
    return DataStoreRepo.years()


@bp.route('/per_country')
def per_country():
    return DataStoreRepo.medals_per_countries()


@bp.route('/per_country/<int:year>')
def per_country_per_year(year):
    return DataStoreRepo.medals_per_countries_per_year(year)
