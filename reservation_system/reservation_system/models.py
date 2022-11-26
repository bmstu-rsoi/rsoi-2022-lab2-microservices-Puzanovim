import uuid
import enum

from sqlalchemy import Column, String, Integer, Enum
from sqlalchemy.dialects.postgresql import UUID, TIMESTAMP

from reservation_system.db import Base


class Status(enum.Enum):
    RENTED = 'RENTED'
    RETURNED = 'RETURNED'
    EXPIRED = 'EXPIRED'


class Reservation(Base):
    __tablename__ = 'reservation'

    id = Column(Integer, autoincrement=True, primary_key=True)
    reservation_uid = Column(UUID(as_uuid=True), default=uuid.uuid4)
    username = Column(String(80), nullable=False)
    book_uid = Column(UUID(as_uuid=True), nullable=False)
    library_uid = Column(UUID(as_uuid=True), nullable=False)
    status = Column(Enum(Status), nullable=False)
    start_date = Column(TIMESTAMP, nullable=False)
    till_date = Column(TIMESTAMP, nullable=False)
