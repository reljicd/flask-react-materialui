from flask import Blueprint, jsonify

from app.db.repos import MedalRepo

bp = Blueprint('medals', __name__, url_prefix='/medals')


@bp.route('/<int:medal_id>')
def by_id(medal_id):
    return jsonify(MedalRepo.one(id=medal_id))


@bp.route('/years')
def years():
    return jsonify(MedalRepo.years())


@bp.route('/per_country')
def per_country():
    return jsonify(MedalRepo.per_countries())


@bp.route('/per_country/<int:year>')
def per_country_per_year(year):
    return jsonify(MedalRepo.per_countries_per_year(year))


@bp.route('/all')
def all_medals():
    paginator = MedalRepo.all()
    return {'page': paginator.page,
            'per_page': paginator.per_page,
            'has_next': paginator.has_next,
            'pages': paginator.pages,
            'items': paginator.items}
