import sqlalchemy.engine
from sqlalchemy import create_engine, text

from constants.EnviornmentCON import EnvironmentCON


class AlchemyEngineConfig:

    @staticmethod
    def generate_config():
        return create_engine(EnvironmentCON.DATABASE_URL)


    @staticmethod
    def make_sure_pg_vector_exists(engine: sqlalchemy.engine.Engine):
        with engine.connect() as connection:
            connection.execute(text("CREATE EXTENSION IF NOT EXISTS vector;"))
            connection.commit()