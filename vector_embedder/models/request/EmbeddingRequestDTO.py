from pydantic import BaseModel



class EmbeddingRequestDTO(BaseModel):
    text: str
