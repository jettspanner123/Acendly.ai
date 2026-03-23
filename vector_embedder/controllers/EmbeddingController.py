from fastapi import APIRouter
from sqlalchemy.orm import Session

from database.AlchemyEngineStore import AlchemyEngineStore
from database.entities.OP_EmbeddingTBL import OP_EmbeddingTBL
from models.response.BaseResponse import BaseResponse
from models.response.EmbeddingResponse import EmbeddingResponse
from models.request.EmbeddingRequestDTO import EmbeddingRequestDTO
from services.EmbeddingService import EmbeddingService

EMBEDDING_ROUTER = APIRouter(prefix="/embedding", tags=["Embedding"])
EMBEDDING_SERVICE = EmbeddingService()
ALCHEMY_ENGINE = AlchemyEngineStore.ALCHEMY_ENGINE

class EmbeddingController:

    @staticmethod
    @EMBEDDING_ROUTER.get("/health", response_model=BaseResponse)
    async def health_check():
        return BaseResponse(success=True, message="Embedding Controller is healthy!")


    @staticmethod
    @EMBEDDING_ROUTER.post("/create", response_model=EmbeddingResponse)
    async def generate_embedding(request: EmbeddingRequestDTO):
        try:
            data = EMBEDDING_SERVICE.generate_embedding(request.text)
            with Session(ALCHEMY_ENGINE) as db:
                new_embedding = OP_EmbeddingTBL(
                    text=request.text,
                    embedding=data
                )
                db.add(new_embedding)
                db.commit()
            return EmbeddingResponse(success=True, message="Embedding generated!", text=request.text, embedding=data)
        except Exception as e:
            return EmbeddingResponse(success=False, message=str(e), text=request.text, embedding=None)
