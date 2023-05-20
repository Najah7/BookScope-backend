from django.db import models as DjangoModels

from core import models as CoreModels


class Author(DjangoModels.Model):
    class Meta:
        db_table = "authors"
        app_label = "core"

    name = DjangoModels.CharField(max_length=200)
    created_at = DjangoModels.DateTimeField(auto_now_add=True)
    updated_at = DjangoModels.DateTimeField(auto_now=True)

    def __str__(self):
        return f"name: {self.name}"
