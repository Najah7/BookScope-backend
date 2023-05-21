from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone

from core.models import (
    ReadBook,
    Book,
    Author,
    Publisher,
)
from core.serializers import (
    BookSerializer,
    ReadBookSerializer,
)
from core.helper import (
    response as res_helper,
    params as param_helper,
    book_api as api_helper,
)


class BookAPIView(APIView):
    def get(self, request):

        if not request.query_params:
            return Response(BookSerializer(Book.objects.all(), many=True).data)

        # TODO: まとめる👇
        book_info = param_helper.get_book_params_handler(request)

        # HACK: しっかりまとめる
        # HACK: 並び順に依存しているので改善するべき👇

        if book_info["book_id"]:
            book = Book.objects.filter(id=book_info["book_id"]).first()
            return Response(BookSerializer(book).data)
        elif book_info["isbn"]:
            book = Book.objects.filter(isbn=book_info["isbn"]).first()
            if book:
                return Response(BookSerializer(book).data)
            else:
                return Response({"message": "本が見つかりませんでした。", "hint": "ISBNを間違えていませんか？"})
        elif book_info["title"]:
            books = Book.objects.search_books_by_title(book_info["title"])
            if books:
                return Response(BookSerializer(books, many=True).data)
            else:
                return {"message": "本が見つかりませんでした。", "hint": "本の名前を間違えていませんか？"}
        elif book_info["author"]:
            books = Book.objects.search_books_by_author(book_info["author"])
            if books:
                return Response(BookSerializer(books, many=True).data)
            else:
                return {"message": "本が見つかりませんでした。", "hint": "著者名を間違えていませんか？"}
        elif book_info["publisher"]:
            books = Book.objects.search_books_by_publisher(book_info["publisher"])
            if books:
                return Response(BookSerializer(books, many=True).data)
            else:
                return {"message": "本が見つかりませんでした。", "hint": "出版社名を間違えていませんか？"}
        

    def post(self, request):
        """読んだ本を登録する（読んだ本からしか本を登録できない仕様）"""

        book_info = param_helper.post_book_params_handler(request)

        # print("=====================================")
        # print(book_info)
        
        if book_info.get("isbn") is not None:
            new_book_info = api_helper.fetch_book_data_by_isbn(book_info["isbn"])
            new_book_info["tags"] = book_info["tags"]
            book_info = new_book_info
                

        # print("=====================================")
        # print(book_info.get("isbn"))
        book = Book.objects.create_book_with_tags(
            title=book_info["title"],
            isbn=book_info["isbn"],
            price=book_info["price"],
            image_url=book_info["image_url"],
            book_tags=book_info["tags"],
        )
        author = Author.objects.create(name=book_info["author"])
        publisher = Publisher.objects.create(name=book_info["publisher"])
        book.authors.add(author)
        book.publishers.add(publisher)
        
        return Response(BookSerializer(book).data, status=status.HTTP_201_CREATED)

        # HACK: ユーザ認証できてなくチェックしているのでそれをどうする
        # # TODO: 読んだ本を作成 by user と book
        # ReadBook.objects.create(
        #     user=request.user,
        #     book=book,
        #     read_at=timezone.now(),
        # )

        # # TODO: 本の情報を返す
        # return Response(ReadBookSerializer(book).data)

    def delete(self, request):
        book_id = request.data.get("book_id")
        if book_id:
            try:
                book = ReadBook.objects.filter(book_id=book_id).first()
                book.delete()
                return Response({"message": "本を削除しました。"}, status=status.HTTP_200_OK)
            except ReadBook.DoesNotExist:
                return Response({"message": "指定された本が存在しません。"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"message": "削除する本のIDが提供されていません。"}, status=status.HTTP_400_BAD_REQUEST)
