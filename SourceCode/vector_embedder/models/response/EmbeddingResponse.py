from typing import List

from models.response.BaseResponse import BaseResponse


class EmbeddingResponse(BaseResponse):
    text: str
    embedding: List[List[float]] | None
