from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, Request, status
from gateway_service.apis import (LibrarySystemAPI, RatingSystemAPI,
                                  get_library_system_api,
                                  get_rating_system_api,
                                  get_reservation_system_api)
from gateway_service.apis.library_system_api.schemas import Book, Library, LibrariesPagination, BooksPagination
from gateway_service.apis.rating_system_api.schemas import UserRating
from gateway_service.apis.reservation_system.api import ReservationSystemAPI
from gateway_service.apis.reservation_system.schemas import (
    Reservation, ReservationBook, ReservationBookInput, ReturnBookInput)
from gateway_service.validators import validate_page_size_params

router = APIRouter()


@router.get('/libraries', status_code=status.HTTP_200_OK, summary='Получить список библиотек в городе')
async def get_libraries(
        city: str,
        page: int = 0,
        size: int = 100,
        library_system_api: LibrarySystemAPI = Depends(get_library_system_api)
) -> LibrariesPagination:
    validate_page_size_params(page, size)
    libraries: LibrariesPagination = await library_system_api.get_libraries(city, page, size)
    return libraries


@router.get('/libraries/{library_id}/books', status_code=status.HTTP_200_OK, summary='Получить список книг в выбранной библиотеке')
async def get_books(
        library_id: str,
        page: int = 0,
        size: int = 100,
        show_all: bool = False,
        library_system_api: LibrarySystemAPI = Depends(get_library_system_api)
) -> BooksPagination:
    validate_page_size_params(page, size)
    books: BooksPagination = await library_system_api.get_books(UUID(library_id), page, size, show_all)
    return books


@router.get('/reservations', status_code=status.HTTP_200_OK, summary='Получить информацию по всем взятым в прокат книгам пользователя')
async def get_reservations(
        request: Request,
        reservation_system_api: ReservationSystemAPI = Depends(get_reservation_system_api)
) -> List[Reservation]:
    name: str = request.headers.get('X-User-Name')
    reservations: List[Reservation] = await reservation_system_api.get_reservations(name)
    return reservations


@router.post('/reservations', status_code=status.HTTP_200_OK, summary='Взять книгу в библиотеке')
async def reservation_book(
        request: Request,
        reservation_book_input: ReservationBookInput,
        reservation_system_api: ReservationSystemAPI = Depends(get_reservation_system_api)
) -> ReservationBook:
    name: str = request.headers.get('X-User-Name')
    reservation: ReservationBook = await reservation_system_api.reserve_book(name, reservation_book_input)

    # except Exception: raise status=400 ERROR(message: str, errors: List[Error(field: str, error: str)])

    return reservation


@router.post('/reservations/{reservation_id}/return', status_code=status.HTTP_204_NO_CONTENT, summary='Вернуть книгу')
async def return_book(
        reservation_id: str,
        request: Request,
        return_book_input: ReturnBookInput,
        reservation_system_api: ReservationSystemAPI = Depends(get_reservation_system_api)
) -> None:
    name: str = request.headers.get('X-User-Name')
    await reservation_system_api.return_book(name, UUID(reservation_id), return_book_input)
    # ERROR status_code=404 Error(message: str)


@router.get('/rating', status_code=status.HTTP_200_OK, summary='Получить рейтинг пользователя')
async def get_rating(
        request: Request,
        rating_system_api: RatingSystemAPI = Depends(get_rating_system_api)
) -> UserRating:
    name: str = request.headers.get('X-User-Name')
    user_rating: UserRating = await rating_system_api.get_rating(name)
    return user_rating
