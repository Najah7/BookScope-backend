from django.db import models as DjangoModels
from django.utils import timezone
from django.conf import settings

from django.contrib.auth import get_user_model

from core import models as CoreModels


class ReadBookModelManager(DjangoModels.Manager):
    # ===================　検索系 ===================

    def search_read_books_by_book_name(self, user_id, book_name):
        return self.filter(user_id=user_id, book__title__contains=book_name).all()

    def search_read_books_by_author_name(self, user_id, author_name):
        return self.filter(
            user_id=user_id, book__authors__name__contains=author_name
        ).all()

    def search_read_books_by_book_tag(self, user_id, tag):
        return self.filter(user_id=user_id, book__book_tags__name__contains=tag).all()

    # ---------------------　単数 ---------------------
    def get_a_read_book(self, user_id, book_id):
        return self.objects.filter(user_id=user_id, book_id=book_id).first()

    def get_a_read_book_by_book_name(self, user_id, book_name):
        return self.objects.filter(
            user_id=user_id, book__title__contains=book_name
        ).first()


class ReadBook(DjangoModels.Model):
    class Meta:
        db_table = "read_books"
        app_label = "core"

    user = DjangoModels.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=DjangoModels.CASCADE,
        related_name="read_books",
    )
    book = DjangoModels.ForeignKey(
        CoreModels.Book, on_delete=DjangoModels.CASCADE, related_name="read_books"
    )
    # NOTE: タイムゾーンに関してWarningが出る。後で調査する
    read_at = DjangoModels.DateTimeField(default=timezone.now)
    created_at = DjangoModels.DateTimeField(auto_now_add=True)
    updated_at = DjangoModels.DateTimeField(auto_now=True)

    objects = ReadBookModelManager()

    def __str__(self):
        return (
            f"user_id: {self.user_id} book_id: {self.book_id} read_at: {self.read_at}"
        )
