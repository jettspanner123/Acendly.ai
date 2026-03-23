import datetime
import uuid

from pgvector.sqlalchemy import Vector
from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from database.entities.DBase import DBase


class OP_EmbeddingTBL(DBase):
    __tablename__ = "op_embeddings"

    def __str__(self):
        return f"OP_EmbeddingTBL(id={self.id}, text={self.text}, embedding={self.embedding}, user_id={self.user_id}, created_at={self.created_at}, updated_at={self.updated_at})"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4())
    text: Mapped[str] = mapped_column(String(1000), nullable=False)
    embedding: Mapped[list] = mapped_column(Vector(768))
    user_id: Mapped[uuid.UUID] = mapped_column()

    created_at: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime.datetime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())
