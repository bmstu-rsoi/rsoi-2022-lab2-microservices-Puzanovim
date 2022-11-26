from typing import List
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from library_system.db.models import Library, Book, LibraryBooks
from library_system.service.schemas import LibraryModel, BookModel


class LibraryRepository:
    async def get_libraries(self, db: AsyncSession, city: str) -> List[LibraryModel]:
        async with db.begin():
            result = await db.execute(select(Library).where(Library.city == city))

        libraries: List[Library] = result.scalars().all()

        return [LibraryModel.from_orm(library) for library in libraries]

    async def get_books(self, db: AsyncSession, library_id: UUID, show_all: bool = False) -> List[BookModel]:
        query = select(LibraryBooks.book_id).where(LibraryBooks.library_id == library_id)

        if not show_all:
            query.where(LibraryBooks.available_count > 0)

        async with db.begin():
            result = await db.execute(query)

        books: List[Book] = result.scalars().all()

        return [BookModel.from_orm(book) for book in books]


library_repository: LibraryRepository = LibraryRepository()


async def get_library_repository() -> LibraryRepository:
    return library_repository
