from enum import Enum
from typing import List
from uuid import UUID

from pydantic import BaseModel


class Condition(Enum):
    EXCELLENT = 'EXCELLENT'
    GOOD = 'GOOD'
    BAD = 'BAD'


class LibraryModel(BaseModel):
    id: int
    library_uid: UUID
    name: str
    city: str
    address: str

    class Config:
        orm_mode = True


class BookModel(BaseModel):
    id: int
    book_uid: UUID
    name: str
    author: str
    genre: str
    condition: Condition

    class Config:
        orm_mode = True


class ListResponse(BaseModel):
    page: int
    pageSize: int
    totalElements: int
    items: List


class LibrariesResponse(ListResponse):
    items: List[LibraryModel]


class BooksResponse(ListResponse):
    items: List[BookModel]
