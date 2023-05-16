from django.db import models

from django.conf import settings


class WroteHistory(models.Model):
    class Meta:
        db_table = "wrote_histories"
        app_label = "core"

    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
