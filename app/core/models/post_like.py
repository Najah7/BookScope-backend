from django.db import models

from django.conf import settings


class PostLike(models.Model):
    class Meta:
        db_table = "post_likes"
        app_label = "core"

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"user_id: {self.user_id} post_id: {self.post_id}"
