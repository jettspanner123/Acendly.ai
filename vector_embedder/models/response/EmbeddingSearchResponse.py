from pydantic import BaseModel

from models.response.BaseResponse import BaseResponse


class EmbeddingSearchResponse(BaseResponse):
    search_text: str
    result_text: str | None
    similarity_score: float | None