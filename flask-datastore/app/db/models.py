from dataclasses import dataclass

from sqlalchemy.orm import Mapped

from app.db.database import db


@dataclass
class Country(db.Model):
    __tablename__ = 'countries'

    id: int
    country: str
    code: str
    population: int
    gdp: float

    id = db.Column(db.BigInteger, primary_key=True)
    country = db.Column(db.String)
    code = db.Column(db.String, unique=True)
    population = db.Column(db.Integer)
    gdp = db.Column(db.Float)


@dataclass
class Medal(db.Model):
    __tablename__ = 'medals'

    id: int
    year: int
    medal: str
    sport: str
    discipline: str
    athlete: str
    country: Mapped[Country]
    gender: str
    event: str
    medal: str

    id = db.Column(db.BigInteger, primary_key=True)
    year = db.Column(db.Integer)
    city = db.Column(db.String)
    sport = db.Column(db.String)
    discipline = db.Column(db.String)
    athlete = db.Column(db.String)
    country_code = db.Column(db.String, db.ForeignKey(Country.code))
    country = db.relationship(lambda: Country)
    gender = db.Column(db.String)
    event = db.Column(db.String)
    medal = db.Column(db.String)
