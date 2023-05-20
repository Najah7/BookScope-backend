from django.db import models


class Publisher(models.Model):
    class Meta:
        db_table = "publishers"
        app_label = "core"

    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"name: {self.name}"
