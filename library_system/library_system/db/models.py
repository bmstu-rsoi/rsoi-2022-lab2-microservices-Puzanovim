import uuid
import enum

from sqlalchemy import Column, String, ForeignKey, Integer, Enum
from sqlalchemy.dialects.postgresql import UUID

from library_system.db.db_config import Base


class Condition(enum.Enum):
    EXCELLENT = 'EXCELLENT'
    GOOD = 'GOOD'
    BAD = 'BAD'


class Library(Base):
    __tablename__ = 'library'

    id = Column(Integer, autoincrement=True, primary_key=True)
    library_uid = Column(UUID(as_uuid=True), default=uuid.uuid4)
    name = Column(String(80), nullable=False)
    city = Column(String(255), nullable=False)
    address = Column(String(255), nullable=False)


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, autoincrement=True, primary_key=True)
    book_uid = Column(UUID(as_uuid=True), nullable=False, default=uuid.uuid4)
    name = Column(String(255), nullable=False)
    author = Column(String(255))
    genre = Column(String(255))
    condition = Column(Enum(Condition), default=Condition.EXCELLENT)


class LibraryBooks(Base):
    __tablename__ = 'library_books'

    id = Column(Integer, autoincrement=True, primary_key=True)
    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)
    library_id = Column(Integer, ForeignKey("library.id"), nullable=False)
    available_count = Column(Integer, nullable=False)
