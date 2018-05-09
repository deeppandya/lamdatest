from sqlalchemy import Table
from sqlalchemy import exc
from sqlalchemy.orm import mapper

import database_engine as database_engine


class Country(object):
    __table_name__ = 'country'


def get_country():
    country = Table(Country.__table_name__, database_engine.metadata, autoload=True)
    mapper(Country, country)

    session = database_engine.Session()
    country = None

    try:
        query_object = session.query(Country.id, Country.name)
        data = as_dict(query_object.first()) if query_object.first() is not None else None
        country = data

    except exc.SQLAlchemyError:
        print("SqlAlchemy database error")

    finally:
        session.close()

    return country


def as_dict(row):
    d = {}
    for column in row.keys():
        d[column] = str(getattr(row, column))

    return d
