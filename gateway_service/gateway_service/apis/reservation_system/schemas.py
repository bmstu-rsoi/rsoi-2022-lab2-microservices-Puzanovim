from enum import Enum
from uuid import UUID

from gateway_service.apis.library_system_api.schemas import (BookInfo,
                                                             Condition,
                                                             Library)
from gateway_service.apis.rating_system_api.schemas import UserRating
from pydantic import BaseModel


class Status(Enum):
    RENTED = 'RENTED'
    RETURNED = 'RETURNED'
    EXPIRED = 'EXPIRED'


class Reservation(BaseModel):
    id: UUID
    status: Status
    start_date: str  # format: ISO 8601
    till_date: str  # format: ISO 8601
    book: BookInfo
    library: Library


class ReservationBookInput(BaseModel):
    book_id: UUID
    library_id: UUID
    till_date: str


class ReturnBookInput(BaseModel):
    condition: Condition
    date: str


class ReservationBook(BaseModel):
    reservation_id: UUID
    status: Status
    start_date: str  # format: ISO 8601
    till_date: str  # format: ISO 8601
    book: BookInfo
    library: Library
    rating: UserRating
