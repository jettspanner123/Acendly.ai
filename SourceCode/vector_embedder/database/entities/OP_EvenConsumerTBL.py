import datetime
import uuid

from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped
from sqlalchemy.testing.schema import mapped_column
from sqlalchemy.sql import func

from database.entities.DBase import DBase


class OP_EventConsumerTBL(DBase):

    __tablename__ = "op_event_consumers"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4(), nullable=False, updatable=False)
    event_name: Mapped[str] = mapped_column(String(1000), nullable=False, updatable=False)

    created_at: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False, updatable=False, server_default=func.now())
    updated_at: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False, updatable=False, gdefault=func.now())
