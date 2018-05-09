from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool, QueuePool

engine_canada = create_engine(
    'mysql+pymysql://sqlalchemytest:SqlAlchemyTest@127.0.0.1/traderev',
    echo=False,
    poolclass=NullPool)

metadata = MetaData(engine_canada)

Session = sessionmaker(bind=engine_canada)


def dispose_engines():
    engine_canada.dispose()
