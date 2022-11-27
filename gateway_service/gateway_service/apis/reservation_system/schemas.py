from datetime import date
from enum import Enum
from uuid import UUID

from gateway_service.apis.library_system_api.schemas import BookModel, Condition, LibraryModel
from gateway_service.apis.rating_system_api.schemas import UserRating
from pydantic import BaseModel


class Status(Enum):
    RENTED = 'RENTED'
    RETURNED = 'RETURNED'
    EXPIRED = 'EXPIRED'


class Reservation(BaseModel):
    reservationUid: UUID
    status: Status
    startDate: date
    tillDate: date


class ReservationModel(BaseModel):
    bookUid: UUID
    libraryUid: UUID


class ReservationResponse(BaseModel):
    book: BookModel
    library: LibraryModel


class ReservationBookInput(BaseModel):
    bookUid: UUID
    libraryUid: UUID
    tillDate: date


class ReturnBookInput(BaseModel):
    condition: Condition
    date: date


class ReservationBook(BaseModel):
    reservationUid: UUID
    status: Status
    startDate: date
    tillDate: date
    book: BookModel
    library: LibraryModel
    rating: UserRating
