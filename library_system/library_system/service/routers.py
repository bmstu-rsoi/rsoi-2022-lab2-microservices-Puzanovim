from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from library_system.db.db_config import async_db_session
from library_system.db.repository import LibraryRepository, get_library_repository
from library_system.service.schemas import LibraryModel, LibrariesResponse, BooksResponse

router = APIRouter()


@router.get('/libraries', status_code=status.HTTP_200_OK, response_model=LibrariesResponse)
async def get_libraries(
        city: str,
        page: int = 1,
        size: int = 100,
        db: AsyncSession = Depends(async_db_session),
        repository: LibraryRepository = Depends(get_library_repository)
) -> LibrariesResponse:
    libraries: List[LibraryModel] = await repository.get_libraries(db, city)

    result_count = len(libraries)

    if result_count < size:
        size = result_count
        page = 1
    else:
        lower_bound = (page - 1) * size
        upper_bound = page * size
        libraries = libraries[lower_bound:upper_bound]

    return LibrariesResponse(page=page, pageSize=size, totalElements=result_count, items=libraries)


@router.get('/libraries/{library_id}/books', status_code=status.HTTP_200_OK, response_model=BooksResponse)
async def get_books(
        library_id: str,
        show_all: bool,
        page: int = 1,
        size: int = 100,
        db: AsyncSession = Depends(async_db_session),
        repository: LibraryRepository = Depends(get_library_repository)
) -> BooksResponse:
    books = await repository.get_books(db, UUID(library_id), show_all)

    result_count = len(books)

    if result_count < size:
        size = result_count
        page = 1
    else:
        lower_bound = (page - 1) * size
        upper_bound = page * size
        books = books[lower_bound:upper_bound]

    return BooksResponse(page=page, pageSize=size, totalElements=result_count, items=books)
