from typing import List
from uuid import UUID

from gateway_service.apis.reservation_system.schemas import (
    Reservation, ReservationBook, ReservationBookInput, ReturnBookInput)


async def smth():
    pass


class ReservationSystemAPI:
    async def get_reservations(self, name: str) -> List[Reservation]:
        reservations: List[Reservation] = await smth()
        return reservations

    async def reserve_book(self, name: str, reservation_book_input: ReservationBookInput) -> ReservationBook:
        reservation_book: ReservationBook = await smth()
        return reservation_book

    async def return_book(self, name: str, reservation_id: UUID, return_book_input: ReturnBookInput) -> None:
        await smth()
