from django.db import models

from core.models import Book


class BookTag(models.Model):
    class Meta:
        db_table = "book_tags"
        app_label = "core"

    user_id = models.ManyToManyField(Book)
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
