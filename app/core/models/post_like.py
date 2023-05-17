from django.db import models

from django.conf import settings
from core.models import Post


class PostLike(models.Model):
    class Meta:
        db_table = "post_likes"
        app_label = "core"

    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="post_likes")
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"user_id: {self.user_id} post_id: {self.post_id}"