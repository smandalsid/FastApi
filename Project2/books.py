from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
from starlette import status

app=FastAPI()

class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    published_date: str

    def __init__(self, id, title, author, description, rating, published_date):
        self.id=id
        self.title=title
        self.author=author
        self.description=description
        self.rating=rating
        self.published_date=published_date

class BookRequest(BaseModel):
    id: Optional[int]=Field(description="ID is not needed on create", default=None)
    title: str=Field(min_length=3)
    author: str=Field(min_length=1)
    description: str=Field(min_length=1, max_length=100)
    rating: int=Field(gt=-1, lt=6)
    published_date: str=Field(min_length=8)

    model_config={
        "json_schema_extra":{
            "example":{
                "title":"A new title",
                "author":"the author of the book",
                "description":"Description of the book",
                "rating":5,
                "published_date": "dd/mm/yy",
            }
        }
    }


BOOKS=[
    Book(1, "Title1", "Author1", "Desc1", 5, "12/12/12"),
    Book(2, "Title2", "Author2", "Desc2", 5, "12/12/12"),
    Book(3, "Title3", "Author3", "Desc3", 5, "12/12/12"),
    Book(4, "Title4", "Author1", "Desc4", 4, "12/12/12"),
    Book(5, "Title5", "Author1", "Desc5", 1, "12/12/12"),
    Book(6, "Title6", "Author4", "Desc6", 2, "12/12/12"),
]

@app.get("/books", status_code=status.HTTP_200_OK)
async def read_all_books():
    return BOOKS

@app.post("/books/create_book", status_code=status.HTTP_201_CREATED)
async def create_book(book_request:BookRequest):
    new_book=Book(**book_request.model_dump())
    BOOKS.append(find_book_id(new_book))

def find_book_id(book:Book):
    book.id=1 if len(BOOKS)==0 else len(BOOKS)+1
    return book

@app.get("/books/{book_id}", status_code=status.HTTP_200_OK)
async def read_book(book_id:int=Path(gt=0)):
    for book in BOOKS:
        if book.id==book_id:
            return book
    raise HTTPException(status_code=404, detail="Item not found")
        
@app.get("/books/", status_code=status.HTTP_200_OK)
async def read_book_by_rating(book_rating:int=Query(gt=0, lt=6)):
    books_to_return=[]
    for book in BOOKS:
        if(book.rating==book_rating):
            books_to_return.append(book)
    return books_to_return


@app.put("/books/update_book", status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book:BookRequest):
    book_changed=False
    for i in range(len(BOOKS)):
        if(BOOKS[i].id==book.id):
            BOOKS[i]=book
            book_changed=True
    if not book_changed:
        raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int=Path(gt=0)):
    book_deleted=False
    for i in range(len(BOOKS)):
        if(BOOKS[i].id==book_id):
            BOOKS.pop(i)
            book_deleted=True
            break
    if not book_deleted:
        raise HTTPException(status_code=404, detail="Item not found")

@app.get("/books/publish/", status_code=status.HTTP_200_OK)
async def read_books_by_publish_date(published_date: str=Query(gt="01/01/01", lt="12/12/24")):
    books_to_return=[]
    for book in BOOKS:
        if(book.published_date==published_date):
            books_to_return.append(book)
    return books_to_return


