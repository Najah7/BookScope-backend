from rest_framework.response import Response

def generate_book_response(book):
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

def generate_book_responses(books):
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
    
def wrong_isbn_response():
    return Response({
        "message": "本が見つかりませんでした。",
        "hint": "ISBNコードが間違っている可能性があります。",
    })