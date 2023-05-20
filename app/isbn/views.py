from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from core.models import (
    ReadBook,
    Book,
)


class BookInfoView(APIView):
    def get(self, request):
        isbn = request.query_params.get("code")
        
        read_book = ReadBook.objects.filter(isbn=isbn).first()
        if read_book:
            return Response(
                {
                    "book_id": read_book.book.id,
                    "title": read_book.book.title,
                    "author": read_book.book.author.name,
                    "publisher": read_book.book.publisher.name,
                    "price": read_book.book.price,
                    "image_url": read_book.book.image_url,
                    "tags": read_book.book.tags,
    
                }
            )
        else:
            # TODO: ここ、外部APIを叩くところ
            book = Book.objects.filter(isbn=isbn).first()
            if book:
                return Response(
                    {
                        "book_id": book.id,
                        "title": book.title,
                        "author": book.author.name,
                        "publisher": book.publisher.name,
                        "price": book.price,
                        "image_url": book.image_url,
                        "tags": book.tags,
                    }
                )
            else:
                not_found_res = {
                    "message": "本が見つかりませんでした。",
                    "hint": "ISBNコードが間違っている可能性があります。",
                }
                return Response(not_found_res, status=status.HTTP_404_NOT_FOUND)

class BookImageAPI(APIView):
    
    def get(self, request):
        isbn = request.query_params.get("isbn")
        
        read_book = ReadBook.objects.filter(isbn=isbn).first()
        
        if read_book:
            return Response(
                {
                    "book_id": read_book.book.id,
                    "image_url": read_book.book.image_url,
                }
            )
        else:
            return Response(
                {
                    "message": "本が見つかりませんでした。",
                    "hint": "この本の画像はこのアプリのデータベースには登録されていない可能性が高いです。"
                }
            )
        

            
class CodeReaderAPI(APIView):
    # TODO: ２次元コードを読み取る用の処理を実装👇
    def post(self, request):
        isbn = request.data.get("code")
        read_book = ReadBook.objects.filter(isbn=isbn).first()
        if read_book:
            return Response(
                {
                    "book_id": read_book.book.id,
                    "title": read_book.book.title,
                    "author": read_book.book.author.name,
                    "publisher": read_book.book.publisher.name,
                    "price": read_book.book.price,
                    "image_url": read_book.book.image_url,
                    "tags": read_book.book.tags,
    
                }
            )
        else:
            response = {
                "message": "バーコードが読み取れませんでした。",
            }
            return Response(response)