from uuid import UUID

from gateway_service.apis.library_system_api.schemas import BooksPagination, LibrariesPagination, BookModel, \
    LibraryModel
from gateway_service.config import LIBRARY_SYSTEM_CONFIG
from httpx import AsyncClient


class LibrarySystemAPI:
    def __init__(self, host: str = LIBRARY_SYSTEM_CONFIG.host, port: int = LIBRARY_SYSTEM_CONFIG.port) -> None:
        self._host = host
        self._port = port

    async def get_libraries(self, city: str, page: int, size: int) -> LibrariesPagination:
        params = {'city': city, 'page': page, 'size': size}
        async with AsyncClient() as client:
            response = await client.get(f'http://{self._host}:{self._port}/libraries', params=params)

        libraries: LibrariesPagination = LibrariesPagination(**response.json())
        return libraries

    async def get_library(self, library_uid: UUID) -> LibraryModel:
        async with AsyncClient() as client:
            response = await client.get(f'http://{self._host}:{self._port}/libraries/{library_uid}')

        library: LibraryModel = LibraryModel(**response.json())
        return library

    async def get_books(self, library_uid: UUID, page: int, size: int, show_all: bool) -> BooksPagination:
        params = {'page': page, 'size': size, 'show_all': show_all}
        async with AsyncClient() as client:
            response = await client.get(f'http://{self._host}:{self._port}/libraries/{library_uid}/books', params=params)

        books: BooksPagination = BooksPagination(**response.json())
        return books

    async def get_book(self, library_uid: UUID, book_uid: UUID) -> BookModel:
        async with AsyncClient() as client:
            response = await client.get(f'http://{self._host}:{self._port}/libraries/{library_uid}/books/{book_uid}')

        book: BookModel = BookModel(**response.json())
        return book
