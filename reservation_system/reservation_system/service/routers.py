from typing import List
from uuid import UUID

from fastapi import APIRouter, status, Depends

from reservation_system.db.repository import ReservationRepository, get_reservation_repository
from reservation_system.service.schemas import ReservationResponse, ReservationModel, ReservationInput, \
    ReservationRequest

router = APIRouter()


@router.get('/reservations', status_code=status.HTTP_200_OK, response_model=List[ReservationResponse])
async def get_reservations(
        username: str, repository: ReservationRepository = Depends(get_reservation_repository)
) -> List[ReservationResponse]:
    reservations: List[ReservationModel] = await repository.get_reservations(username)
    reservations_response: List[ReservationResponse] = [
        ReservationResponse(
            **reservation.dict(exclude={'id', 'reservation_uid'}), reservationUid=reservation.reservation_uid
        ) for reservation in reservations
    ]
    return reservations_response


@router.get('/reservations/{reservation_uid}', status_code=status.HTTP_200_OK, response_model=ReservationResponse)
async def get_reservation(
        reservation_uid: str,
        repository: ReservationRepository = Depends(get_reservation_repository)
) -> ReservationResponse:
    reservation: ReservationModel = await repository.get_reservation(UUID(reservation_uid))
    return ReservationResponse(
        **reservation.dict(exclude={'id', 'reservation_uid'}), reservationUid=reservation.reservation_uid
    )


@router.post('/reservations', status_code=status.HTTP_201_CREATED, response_model=ReservationResponse)
async def get_reservation(
        username: str,
        reservation_request: ReservationRequest,
        repository: ReservationRepository = Depends(get_reservation_repository)
) -> ReservationResponse:
    reservation_input: ReservationInput = ReservationInput(**reservation_request.dict(), username=username)
    reservation: ReservationModel = await repository.create_reservation(reservation_input)
    return ReservationResponse(
        **reservation.dict(exclude={'id', 'reservation_uid'}), reservationUid=reservation.reservation_uid
    )


@router.post('/reservations', status_code=status.HTTP_201_CREATED, response_model=ReservationResponse)
async def get_reservation(
        username: str,
        reservation_request: ReservationRequest,
        repository: ReservationRepository = Depends(get_reservation_repository)
) -> ReservationResponse:
    reservation_input: ReservationInput = ReservationInput(**reservation_request.dict(), username=username)
    reservation: ReservationModel = await repository.create_reservation(reservation_input)
    return ReservationResponse(
        **reservation.dict(exclude={'id', 'reservation_uid'}), reservationUid=reservation.reservation_uid
    )
