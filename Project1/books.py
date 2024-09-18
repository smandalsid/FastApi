from fastapi import FastAPI, Body

app=FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]

# GET request
# GET requests cant take Body

@app.get("/books")
async def read_all_books():
    return BOOKS

@app.get("/books/{book_title}") # path parameters
async def read_book(book_title:str):
    for book in BOOKS:
        if(book.get('title').casefold()==book_title.casefold()):
            return book

@app.get("/books/by_author/{author_name}")
async def read_books_by_author(author_name:str):
    books_to_return=[]
    for book in BOOKS:
        if(book.get('author').casefold()==author_name.casefold()):
            books_to_return.append(book)
    return books_to_return


@app.get("/books/") # query parameters
async def read_category_by_query(category:str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold()==category.casefold():
            books_to_return.append(book)
    return books_to_return


# search by the author and filter by the category

@app.get("/books/{author_name}/")
async def read_author_category_by_query(author_name:str, category:str):
    books_to_return=[]
    for book in BOOKS:
        if book.get('category').casefold()==category.casefold() and book.get('author').casefold()==author_name.casefold():
            books_to_return.append(book)
    return books_to_return


# POST REQUEST

@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)


# PUT request

@app.put("/books/update_book")
async def update_books(updated_book=Body()):
    for i in range(len(BOOKS)):
        if(BOOKS[i].get('title').casefold()==updated_book.get('title').casefold()):
            BOOKS[i]=updated_book
    

# DELETE request

@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title:str):
    for i in range(len(BOOKS)):
        if(BOOKS[i].get('title').casefold()==book_title.casefold()):
            BOOKS.pop(i)
            break

