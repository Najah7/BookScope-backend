from django.db import models

from django.conf import settings


class School(models.Model):
    class Meta:
        db_table = "school"
        app_label = "core"

    user_id = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="school")
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def str(self):
        return f"name: {self.name} user_id: {self.user_id}"