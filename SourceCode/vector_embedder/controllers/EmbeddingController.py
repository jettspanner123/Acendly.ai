import uuid

from fastapi import APIRouter
from sqlalchemy.orm import Session
from sqlalchemy import select as Select

from database.AlchemyEngineStore import AlchemyEngineStore
from database.entities.OP_EmbeddingTBL import OP_EmbeddingTBL
from models.request.EmbeddingSearchRequestDTO import EmbeddingSearchRequestDTO
from models.response.BaseResponse import BaseResponse
from models.response.EmbeddingResponse import EmbeddingResponse
from models.request.EmbeddingRequestDTO import EmbeddingRequestDTO
from models.response.EmbeddingSearchResponse import EmbeddingSearchResponse
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
            text_lower = request.text.lower()
            data = EMBEDDING_SERVICE.generate_embedding(text_lower)
            with Session(ALCHEMY_ENGINE) as db:
                new_embedding = OP_EmbeddingTBL(
                    text=request.text,  # Store original text
                    embedding=data[0],
                    user_id=uuid.uuid4()
                )
                db.add(new_embedding)
                db.commit()
            return EmbeddingResponse(success=True, message="Embedding generated!", text=request.text, embedding=data)
        except Exception as e:
            return EmbeddingResponse(success=False, message=str(e), text=request.text, embedding=None)

    @staticmethod
    @EMBEDDING_ROUTER.get("/search", response_model=EmbeddingSearchResponse)
    async def query_embedding(request: EmbeddingSearchRequestDTO):
        text_lower = request.text.lower()
        query_vector = EMBEDDING_SERVICE.generate_embedding(text_lower)[0]
        stmt = (
            Select(OP_EmbeddingTBL)
            .order_by(OP_EmbeddingTBL.embedding.cosine_distance(query_vector))
            .limit(5)
        )
        try:
            with Session(ALCHEMY_ENGINE) as db:
                results = db.execute(stmt).all()
                first_result = results[0][0].text  # Access the text attribute
                return EmbeddingSearchResponse(success=True, message="Embedding search completed!", search_text=request.text,
                                               result_text=first_result, similarity_score=100)
        except Exception as e:
            return EmbeddingSearchResponse(success=False, message="Embedding search failed!",
                                           search_text=request.text, result_text=None, similarity_score=None)
