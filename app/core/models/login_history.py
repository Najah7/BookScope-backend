from django.db import models

from django.conf import settings


class LoginHistory(models.Model):
    class Meta:
        db_table = "wrote_histories"
        app_label = "core"

    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="wrote_histories")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"user_id: {self.user_id}"