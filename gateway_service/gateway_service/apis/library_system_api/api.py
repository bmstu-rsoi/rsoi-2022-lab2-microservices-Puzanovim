from uuid import UUID

from gateway_service.apis.library_system_api.schemas import LibrariesPagination, BooksPagination


async def smth():
    pass


class LibrarySystemAPI:
    async def get_libraries(self, city: str, page: int, size: int) -> LibrariesPagination:
        library: LibrariesPagination = await smth()
        return library

    async def get_books(self, library_id: UUID, page: int, size: int, show_all: bool) -> BooksPagination:
        books: BooksPagination = await smth()
        return books
