from django.db import models
from django.conf import settings

from core.models.book import Book


class ReadBook(models.Model):
    class Meta:
        db_table = "read_books"
        app_label = "core"

    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="read_books")
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="read_books")
    read_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"user_id: {self.user_id} book_id: {self.book_id} read_at: {self.read_at}"