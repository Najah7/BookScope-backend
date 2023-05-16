from django.db import models

from django.conf import settings


class Major(models.Model):
    class Meta:
        db_table = "major"
        app_label = "core"

    user_id = models.ManyToManyField(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
