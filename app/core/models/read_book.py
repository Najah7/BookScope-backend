from django.db import models
from django.conf import settings

from core.models.book import Book


class ReadBook(models.Model):
    class Meta:
        db_table = "read_books"
        app_label = "core"

    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    read_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
