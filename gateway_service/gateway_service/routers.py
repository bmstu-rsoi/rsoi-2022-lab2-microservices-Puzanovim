import logging
from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, status, Header
from gateway_service.apis import (
    LibrarySystemAPI,
    RatingSystemAPI,
    ReservationSystemAPI,
    get_library_system_api,
    get_rating_system_api,
    get_reservation_system_api,
)
from gateway_service.apis.library_system_api.schemas import BooksPagination, LibrariesPagination
from gateway_service.apis.rating_system_api.schemas import UserRating
from gateway_service.apis.reservation_system.schemas import (
    ReservationBook,
    ReservationBookInput,
    ReturnBookInput, ReservationResponse, ReservationModel,
)
from gateway_service.validators import validate_page_size_params

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get(
    '/libraries',
    status_code=status.HTTP_200_OK,
    response_model=LibrariesPagination,
    summary='Получить список библиотек в городе'
)
async def get_libraries(
    city: str, page: int = 0, size: int = 100, library_system_api: LibrarySystemAPI = Depends(get_library_system_api)
) -> LibrariesPagination:
    validate_page_size_params(page, size)
    libraries: LibrariesPagination = await library_system_api.get_libraries(city, page, size)
    return libraries


@router.get(
    '/libraries/{library_uid}/books',
    status_code=status.HTTP_200_OK,
    response_model=BooksPagination,
    summary='Получить список книг в выбранной библиотеке',
)
async def get_books(
    library_uid: str,
    page: int = 0,
    size: int = 100,
    show_all: bool = False,
    library_system_api: LibrarySystemAPI = Depends(get_library_system_api),
) -> BooksPagination:
    validate_page_size_params(page, size)
    books: BooksPagination = await library_system_api.get_books(UUID(library_uid), page, size, show_all)
    return books


@router.get(
    '/reservations',
    status_code=status.HTTP_200_OK,
    response_model=ReservationResponse,
    summary='Получить информацию по всем взятым в прокат книгам пользователя',
)
async def get_reservations(
        x_user_name: str = Header(),
        reservation_system_api: ReservationSystemAPI = Depends(get_reservation_system_api),
        library_system_api: LibrarySystemAPI = Depends(get_library_system_api),
) -> List[ReservationResponse]:
    reservations: List[ReservationModel] = await reservation_system_api.get_reservations(x_user_name)
    return [
        ReservationResponse(
            **reservation.dict(exclude={'libraryUid', 'bookUid'}),
            book=(await library_system_api.get_book(reservation.libraryUid, reservation.bookUid)),
            library=(await library_system_api.get_library(reservation.libraryUid)),
        ) for reservation in reservations
    ]


@router.post('/reservations', status_code=status.HTTP_200_OK, summary='Взять книгу в библиотеке')
async def reservation_book(
    reservation_book_input: ReservationBookInput,
    x_user_name: str = Header(),
    reservation_system_api: ReservationSystemAPI = Depends(get_reservation_system_api),
) -> ReservationBook:
    reservation: ReservationBook = await reservation_system_api.reserve_book(x_user_name, reservation_book_input)

    # except Exception: raise status=400 ERROR(message: str, errors: List[Error(field: str, error: str)])

    return reservation


@router.post('/reservations/{reservation_id}/return', status_code=status.HTTP_204_NO_CONTENT, summary='Вернуть книгу')
async def return_book(
    reservation_id: str,
    return_book_input: ReturnBookInput,
    x_user_name: str = Header(),
    reservation_system_api: ReservationSystemAPI = Depends(get_reservation_system_api),
) -> None:
    await reservation_system_api.return_book(x_user_name, UUID(reservation_id), return_book_input)
    # ERROR status_code=404 Error(message: str)


@router.get('/rating', status_code=status.HTTP_200_OK, summary='Получить рейтинг пользователя')
async def get_rating(
    x_user_name: str = Header(), rating_system_api: RatingSystemAPI = Depends(get_rating_system_api)
) -> UserRating:
    user_rating: UserRating = await rating_system_api.get_rating(x_user_name)
    return user_rating
