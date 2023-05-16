from django.db import models

from core.models import Book


class Publisher(models.Model):
    class Meta:
        db_table = "publishers"
        app_label = "core"

    book_id = models.ManyToManyField(Book)
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
