from sqlalchemy.orm import clear_mappers

import country_db as country_db


def lambda_handler(event, context):
    try:
        return country_db.get_country()
    finally:
        clear_mappers()
        '''
        In the case of Queuepool, engine.dispose() will close all the checked-in connections.
        '''
        # database_engine.dispose_engines()


if __name__ == "__main__":
    print(lambda_handler(None, None))
