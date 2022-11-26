from enum import Enum
from typing import List
from uuid import UUID

from pydantic import BaseModel


class Condition(Enum):
    EXCELLENT = 'EXCELLENT'
    GOOD = 'GOOD'
    BAD = 'BAD'


class Library(BaseModel):
    id: UUID
    name: str
    address: str
    city: str


class BookInfo(BaseModel):
    id: UUID
    name: str
    author: str
    genre: str


class Book(BookInfo):
    condition: Condition
    avaiblableCount: int


class Pagination(BaseModel):
    page: int
    pageSize: int
    totalElements: int


class LibrariesPagination(Pagination):
    items: List[Library]


class BooksPagination(Pagination):
    items: List[Book]
