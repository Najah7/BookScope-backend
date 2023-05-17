from django.db import models

from core.models import Book


class BookTag(models.Model):
    class Meta:
        db_table = "book_tags"
        app_label = "core"

    book_id = models.ManyToManyField(Book, related_name="book_tags")
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"tag: {self.name} book_id: {self.book_id}"
