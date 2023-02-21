import os
from dataclasses import dataclass
from typing import Any, List, TypeVar

from flask import request
from flask_sqlalchemy.pagination import Pagination
from sqlalchemy import text
from sqlalchemy.orm import Query

from app.db.database import db
from app.db.models import Country, Medal

T = TypeVar('T', bound='Base')


class Repo(object):
    _model = None

    @classmethod
    def query(cls, *criterion: Any, **kwargs) -> Query:
        return db.session.query(cls._model).filter(*criterion).filter_by(
            **kwargs)

    @classmethod
    def one(cls, *criterion: Any, **kwargs) -> T:
        return cls.query(*criterion, **kwargs).one()

    @classmethod
    def all(cls, *criterion: Any, page: int = None, per_page: int = None,
            **kwargs) -> Pagination:
        if request:
            page = page if page else request.args.get('page', 1, type=int)
            per_page = per_page if per_page else request.args.get(
                'per_page', 10, type=int)
        return cls.query(*criterion, **kwargs).paginate(
            page=page, per_page=per_page)

    @classmethod
    def count(cls, *criterion, **kwargs) -> int:
        return cls.query(*criterion, **kwargs).count()


class CountryRepo(Repo):
    _model = Country


@dataclass
class CountryMedals:
    country: str
    gold_medals: int = 0
    silver_medals: int = 0
    bronze_medals: int = 0
    population: int = None


class MedalRepo(Repo):
    _model = Medal

    @classmethod
    def years(cls) -> List[int]:
        return [year_tuple[0] for year_tuple
                in cls._model.query.with_entities(cls._model.year).distinct()]

    # For big tables this should be calculated declaratively using SQL
    @classmethod
    def per_countries(cls) -> List[CountryMedals]:
        with open(os.path.join(os.path.dirname(__file__),
                               'sql/medals_per_countries.sql')) as file:
            results = db.session.execute(text(file.read()))
            return [CountryMedals(row.country,
                                  row.gold_medals,
                                  row.silver_medals,
                                  row.bronze_medals,
                                  row.population)
                    for row in results]

    @classmethod
    def per_countries_per_year(cls, year: int) -> List[CountryMedals]:
        with open(os.path.join(
                os.path.dirname(__file__),
                'sql/medals_per_countries_per_year.sql')) as file:
            results = db.session.execute(
                text(file.read()).bindparams(year=year))
            return [CountryMedals(row.country,
                                  row.gold_medals,
                                  row.silver_medals,
                                  row.bronze_medals,
                                  row.population)
                    for row in results]

    # For individual years number of rows is manageable,
    # so I did it dynamically for illustration purposes (it is still slow)
    @classmethod
    def per_countries_per_year_alt(
            cls, year: int) -> List[CountryMedals]:
        country_country_medals = dict()
        for medal in cls.query(year=year):
            if medal.country:
                country = medal.country.country
                population = medal.country.population
                country_medals = country_country_medals.setdefault(
                    country, CountryMedals(country, population=population))
                if medal.medal == 'Gold':
                    country_medals.gold_medals += 1
                if medal.medal == 'Silver':
                    country_medals.silver_medals += 1
                if medal.medal == 'Bronze':
                    country_medals.bronze_medals += 1

        return [country_medals for country_medals
                in country_country_medals.values()
                if (country_medals.gold_medals
                    or country_medals.bronze_medals
                    or country_medals.silver_medals)]
