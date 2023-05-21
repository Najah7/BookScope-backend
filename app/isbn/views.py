import os
import requests

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from pyzbar import pyzbar
from PIL import Image

from core.models import (
    ReadBook,
    Book,
    Author,
    Publisher,
)
from core.helper import response as res_helper
from core.serializers import BookSerializer, ReadBookSerializer

# env_path = '../.env'  # 一時的に。alpineの環境でdotenvを上手くインストールできず

# with open(env_path, 'r') as file:
#     for line in file:
#         line = line.strip()  # 行末の改行文字を削除
#         if line and not line.startswith('#'):
#             key, value = line.split('=', 1)  # キーと値に分割
#             os.environ[key] = value  # 環境変数に追加

class BookInfoView(APIView):
    def get(self, request):
        isbn = request.query_params.get("isbn")
        
        book = ReadBook.objects.filter(book__isbn=isbn).first()
        
        if book:
            return Response(ReadBookSerializer(book).data)
        else:
            # TODO: ここ、外部APIを叩くところ
            app_id = os.environ.get("RAKUTEN_APP_ID")
            response = requests.get(f'https://app.rakuten.co.jp/services/api/BooksBook/Search/20170404?format=json&isbn={int(isbn)}&applicationId={app_id}').json()
            if response.get("Items"):
                book_info = res_helper.format_api_response(response)
                author = Author.objects.get_or_create(name=book_info["author"])
                publisher = Publisher.objects.get_or_create(name=book_info["publisher"])
                book = Book.objects.get_or_create(
                    isbn=isbn,
                    title=book_info["title"],
                    price=book_info["price"],
                    image_url=book_info["image_url"],
                )
                book.authors.add(author)
                book.publishers.add(publisher)
                
                return Response(BookSerializer(book).data)
            else:
                not_found_res = {
                    "message": "本が見つかりませんでした。",
                    "hint": "ISBNコードが間違っている可能性があります。",
                }
                return Response(not_found_res, status=status.HTTP_404_NOT_FOUND)

class BookImageView(APIView):
    
    def get(self, request):
        isbn = request.query_params.get("isbn")
        
        read_book = ReadBook.objects.filter(book__isbn=isbn).first()
        
        if read_book:
            serialized_read_book = ReadBookSerializer(read_book).data
            return Response({
                'id': serialized_read_book['book']['id'],
                'title': serialized_read_book['book']['title'],
                'image_url': serialized_read_book['book']['image_url'],   
            })
        else:
            return Response(
                {
                    "message": "本が見つかりませんでした。",
                    "hint": "この本の画像はこのアプリのデータベースには登録されていない可能性が高いです。"
                }
            )
        

            
class BarcodeView(APIView):
    # TODO: ２次元コードを読み取る用の処理を実装👇
    def post(self, request):
        image = request.FILES.get("image")
        
        pil_image = Image.open(image)
        barcodes = pyzbar.decode(pil_image)
        
        if barcodes:
            barcode_data = barcodes[0].data.decode("utf-8")
            return Response({"isbn": barcode_data})
        else:
            return Response({
                "message": "バーコードが読み取れませんでした。",
            })
        