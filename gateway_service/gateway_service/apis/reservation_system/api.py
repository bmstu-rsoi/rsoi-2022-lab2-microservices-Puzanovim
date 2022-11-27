from typing import List
from uuid import UUID

from httpx import AsyncClient

from gateway_service.apis.reservation_system.schemas import (
    ReservationBook,
    ReservationBookInput,
    ReturnBookInput, ReservationModel,
)
from gateway_service.config import RESERVATION_SYSTEM_CONFIG


class ReservationSystemAPI:
    def __init__(self, host: str = RESERVATION_SYSTEM_CONFIG.host, port: int = RESERVATION_SYSTEM_CONFIG.port) -> None:
        self._host = host
        self._port = port

    async def get_reservations(self, name: str) -> List[ReservationModel]:
        params = {'username': name}
        async with AsyncClient() as client:
            response = await client.get(f'http://{self._host}:{self._port}/reservations', params=params)

        reservations: List[ReservationModel] = response.json()
        return reservations

    async def reserve_book(self, name: str, reservation_book_input: ReservationBookInput) -> ReservationBook:
        params = {'username': name}
        async with AsyncClient() as client:
            response = await client.post(
                f'http://{self._host}:{self._port}/reservations',
                params=params,
                data=reservation_book_input.dict()
            )

        reservation_book: ReservationBook = ReservationBook(**response.json())
        return reservation_book

    async def return_book(self, name: str, reservation_id: UUID, return_book_input: ReturnBookInput) -> None:
        params = {'username': name}
        async with AsyncClient() as client:
            response = await client.post(
                f'http://{self._host}:{self._port}/reservations/{reservation_id}/return',
                params=params,
                data=return_book_input.dict()
            )

        if response.status_code == 204:
            return None
        elif response.status_code == 404:
            pass
            # return ErrorResponse(**response.json())
