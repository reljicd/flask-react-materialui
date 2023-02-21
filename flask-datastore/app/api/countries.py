from flask import Blueprint, jsonify

from app.db.repos import CountryRepo

bp = Blueprint('countries', __name__, url_prefix='/countries')


@bp.route('/<int:country_id>')
def by_id(country_id):
    return jsonify(CountryRepo.one(id=country_id))


@bp.route('/code/<string:code>')
def by_code(code):
    return jsonify(CountryRepo.one(code=code.upper()))


@bp.route('/all')
def all_countries():
    paginator = CountryRepo.all()
    return {'page': paginator.page,
            'per_page': paginator.per_page,
            'has_next': paginator.has_next,
            'pages': paginator.pages,
            'items': paginator.items}
