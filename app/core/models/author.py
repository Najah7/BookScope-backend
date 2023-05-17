from django.db import models

from core.models import Book


class Author(models.Model):
    class Meta:
        db_table = "authors"
        app_label = "core"

    book_id = models.ManyToManyField(Book, related_name="authors")
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"name: {self.name} book_id: {self.book_id}"
