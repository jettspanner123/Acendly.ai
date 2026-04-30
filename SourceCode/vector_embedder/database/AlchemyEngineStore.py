import sqlalchemy

from config.AlchemyEngineConfig import AlchemyEngineConfig


class AlchemyEngineStore:
    ALCHEMY_ENGINE: sqlalchemy.engine.Engine = AlchemyEngineConfig.generate_config()
