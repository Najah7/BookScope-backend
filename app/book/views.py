from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from core.models import (
    ReadBook,
    Book,
)
from core.helper import response as res_helper

class BookView(APIView):
    
    def get(self, request):
       # TODO: まとめる👇 
       book_id = request.query_params.get("book_id")
       isbn = request.query_params.get("isbn")
       book_name = request.query_params.get("book_name")
       author = request.query_params.get("author")
       publisher = request.query_params.get("publisher")
       search = request.query_params.get("search")
       
        # HACK: しっかりまとめる👇
       
       if book_id:
           book = Book.objects.filter(id=book_id).first()
           return res_helper.generate_book_response(book)
       elif isbn:
              read_book = ReadBook.objects.filter(isbn=isbn).first()
              if read_book:
                return res_helper.generate_book_response(read_book.book)
              else:
                  return Response(
                        res_helper.wrong_isbn_response(),
                    )
       elif book_name:
           books = Book.objects.search_books_by_title(book_name)
           if books:
               return res_helper.generate_book_responses(books)
           else:
               return {
                    "message": "本が見つかりませんでした。",
                    "hint": "本の名前を間違えていませんか？"
                }
       elif author:
           books = Book.objects.search_books_by_author(author)
           if books:
               return res_helper.generate_book_responses(books)
           else:
               return {
                    "message": "本が見つかりませんでした。",
                    "hint": "著者名を間違えていませんか？"
                }
       elif publisher:
           books = Book.objects.search_books_by_publisher(publisher)
           if books:
               return res_helper.generate_book_responses(books)
           else:
               return {
                    "message": "本が見つかりませんでした。",
                    "hint": "出版社名を間違えていませんか？"
                }
       elif search:
           books = Book.objects.filter(title__icontains=search)
           if books:
               return Response(
                   [
                       res_helper.generate_book_response(book)
                       for book in books
                ]
                )
           else:
               return Response(
                    {
                        "message": "本が見つかりませんでした。",
                        "hint": "ISBNコードが間違っている可能性があります。",
                    }
                )
    
    def post(self, request):
        
        # TODO: 本を取得 or 作成 
        
        # TODO: 読んだ本を作成 by user と book
        
        # TODO: 本の情報を返す
        
        pass
    
    def delete(self, request):
        book_id = request.query_params.get("book_id")
        ReadBook.objects.filter(book_id=book_id).delete()
            