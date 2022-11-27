from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, status
from library_system.db.repository import LibraryRepository, get_library_repository
from library_system.service.schemas import BookInfo, BooksResponse, LibrariesResponse, LibraryModel, LibraryResponse, \
    BookInfoResponse, BookModel, BookResponse

router = APIRouter()


@router.get('/libraries', status_code=status.HTTP_200_OK, response_model=LibrariesResponse)
async def get_libraries(
    city: str,
    page: int = 1,
    size: int = 100,
    repository: LibraryRepository = Depends(get_library_repository),
) -> LibrariesResponse:
    libraries: List[LibraryModel] = await repository.get_libraries(city)
    libraries_response: List[LibraryResponse] = [
        LibraryResponse(**library.dict(exclude={'id', 'library_uid'}), libraryUid=library.library_uid)
        for library in libraries
    ]

    result_count = len(libraries_response)

    if result_count < size:
        size = result_count
        page = 1
    else:
        lower_bound = (page - 1) * size
        upper_bound = page * size
        libraries_response = libraries_response[lower_bound:upper_bound]

    return LibrariesResponse(page=page, pageSize=size, totalElements=result_count, items=libraries_response)


@router.get('/libraries/{library_uid}', status_code=status.HTTP_200_OK, response_model=LibraryResponse)
async def get_library(
    library_uid: str,
    repository: LibraryRepository = Depends(get_library_repository),
) -> LibraryResponse:
    library: LibraryModel = await repository.get_library(UUID(library_uid))
    return LibraryResponse(**library.dict(exclude={'id', 'library_uid'}), libraryUid=library.library_uid)


@router.get('/libraries/{library_uid}/books', status_code=status.HTTP_200_OK, response_model=BooksResponse)
async def get_books(
    library_uid: str,
    show_all: bool,
    page: int = 1,
    size: int = 100,
    repository: LibraryRepository = Depends(get_library_repository),
) -> BooksResponse:
    books: List[BookInfo] = await repository.get_books(UUID(library_uid), show_all)
    books_response: List[BookInfoResponse] = [
        BookInfoResponse(**book.dict(exclude={'id', 'book_uid'}), bookUid=book.book_uid)
        for book in books
    ]

    result_count = len(books_response)

    if result_count < size:
        size = result_count
        page = 1
    else:
        lower_bound = (page - 1) * size
        upper_bound = page * size
        books_response = books_response[lower_bound:upper_bound]

    return BooksResponse(page=page, pageSize=size, totalElements=result_count, items=books_response)


@router.get('/libraries/{library_uid}/books/{book_uid}', status_code=status.HTTP_200_OK, response_model=BookResponse)
async def get_book(
    library_uid: str,
    book_uid: str,
    repository: LibraryRepository = Depends(get_library_repository),
) -> BookResponse:
    book: BookModel = await repository.get_book(UUID(book_uid))
    return BookResponse(**book.dict(exclude={'id', 'book_uid'}), bookUid=book.book_uid)
