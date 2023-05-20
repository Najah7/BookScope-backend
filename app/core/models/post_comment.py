from django.db import models

from django.conf import settings


class PostComment(models.Model):
    class Meta:
        db_table = "post_comments"
        app_label = "core"

    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (
            f"user_id: {self.user_id} post_id: {self.post_id} comment: {self.comment}"
        )
