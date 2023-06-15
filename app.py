from robyn import Robyn, status_codes
from controllers import all_books, new_book, book_by_id, delete_book, update_book
import json
from robyn.robyn import Response

app = Robyn(__file__)


@app.get("/")
async def hello():
    return Response(status_code=status_codes.HTTP_200_OK, headers={}, body="Hello, World!")

@app.post("/book")
async def create_book(request):
    
    body = request.body
    
    json_body = json.loads(body)
    
    try:
        book = new_book(json_body['title'], json_body['author'])
        return Response(status_code = status_codes.HTTP_200_OK, headers = {}, body = book)
    except:
        return Response(status_code = status_codes.HTTP_500_INTERNAL_SERVER_ERROR, headers = {}, body = "Internal Server Error")


@app.get("/book")
async def books(request):
    
    books = all_books()
    
    return Response(status_code = status_codes.HTTP_200_OK, headers= {}, body = books)


@app.get("/book/:id")
async def get_book(request):
    id = request.path_params["id"]
    book = book_by_id(id)

    try:
        if book == None:
            return Response(status_code = status_codes.HTTP_404_NOT_FOUND, headers = {}, body= "Book not Found")
        else:
            return Response(status_code = status_codes.HTTP_200_OK, headers = {}, body = book)

    except:
        return Response(status_code = status_codes.HTTP_500_INTERNAL_SERVER_ERROR, headers = {}, body = "Internal Server Error")
    
@app.put("/book/:id")
async def update(request):
    id = request.path_params["id"]

    body = request.body
    json_body = json.loads(body)

    title = json_body['title']
    author = json_body['author']

    book_id = book_by_id(id)

    if book_id == None:
        return Response(status_code = status_codes.HTTP_404_NOT_FOUND, headers = {}, body = "Book not Found")
    else:
        try: 
            book = update_book(title, author, id)
            return Response(status_code = status_codes.HTTP_200_OK, headers = {}, body = book)
        except:
            return Response(status_code = status_codes.HTTP_500_INTERNAL_SERVER_ERROR, headers = {}, body = "Internal Server Error")
    

@app.delete("/book/:id")
async def delete(request):
    id = request.path_params["id"]

    book_id = book_by_id(id)

    if book_id == None:
        return Response(status_code = status_codes.HTTP_404_NOT_FOUND, headers = {}, body = "Book not Found")
    else:
        try: 
            delete_book(id)
            return Response(status_code = status_codes.HTTP_200_OK, headers = {}, body = "Book deleted")
        except:
            return Response(status_code = status_codes.HTTP_500_INTERNAL_SERVER_ERROR, headers = {}, body = "Internal Server Error")    



app.start(port=8000, url="0.0.0.0")