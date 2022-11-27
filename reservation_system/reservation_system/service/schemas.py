from datetime import date
from uuid import UUID

from pydantic import BaseModel

from reservation_system.db.models import Status


class ReservationRequest(BaseModel):
    book_uid: UUID
    library_uid: UUID
    till_date: date

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class ReservationInput(ReservationRequest):
    username: str
    status: Status = Status.RENTED
    start_date: date = date.today()


class ReservationModel(ReservationInput):
    id: int
    reservation_uid: UUID


class ReservationUpdate(BaseModel):
    status: Status


class ReservationResponse(ReservationInput):
    reservationUid: UUID
