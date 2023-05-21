from rest_framework.response import Response


def generate_book_response_from_obj(book):
    return Response({
        "book_id": book.id,
        "title": book.title,
        "isbn": book.isbn,
        "author": book.authors.name,
        "publisher": book.publishers.name,
        "price": book.price,
        "image_url": book.image_url,
        "tags": book.tags,
        })

def generate_book_responses_from_objs(books):
    res_books = []
    for book in books:
        res_book = {
            "book_id": book.id,
            "title": book.title,
            "isbn": book.isbn,
            "author": book.authors.name,
            "publisher": book.publishers.name,
            "price": book.price,
            "image_url": book.image_url,
            "tags": book.tags,
        }
        res_books.append(res_book)
    return Response(res_books)

def format_api_response(api_res):
    book_info = api_res["Items"][0]["Item"]
    title = book_info["title"]
    author = book_info["author"]
    publisher = book_info["publisherName"]
    price = book_info["itemPrice"]
    image_url = book_info["largeImageUrl"]
    
    return {
        "title": title,
        "author": author,
        "publisher": publisher,
        "price": price,
        "image_url": image_url
    }

def wrong_isbn_response():
    return Response({
        "message": "本が見つかりませんでした。",
        "hint": "ISBNコードが間違っている可能性があります。",
    })