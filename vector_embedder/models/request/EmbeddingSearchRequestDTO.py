from pydantic import BaseModel



class EmbeddingSearchRequestDTO(BaseModel):
    text: str