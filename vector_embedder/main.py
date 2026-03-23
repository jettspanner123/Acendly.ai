import sqlalchemy.engine
from fastapi import FastAPI

from config.AlchemyEngineConfig import AlchemyEngineConfig
from controllers.AIController import ai_router
from controllers.EmbeddingController import EMBEDDING_ROUTER
from database.AlchemyEngineStore import AlchemyEngineStore
from database.entities.DBase import DBase
from helpers.EnviornmentVariables import EnvironmentVariableValidator

application = FastAPI()

# Fallback
EnvironmentVariableValidator.validate_env_variables()

# Configurations
AlchemyEngine = AlchemyEngineStore.ALCHEMY_ENGINE
DBase.metadata.create_all(AlchemyEngine)
AlchemyEngineConfig.make_sure_pg_vector_exists(AlchemyEngine)

# Adding Controllers
application.include_router(ai_router)
application.include_router(EMBEDDING_ROUTER)
