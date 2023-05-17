from django.db import models

from django.conf import settings
from core.models import ReadBook


class Post(models.Model):
    class Meta:
        db_table = "posts"
        app_label = "core"

    book_id = models.ForeignKey(ReadBook, on_delete=models.CASCADE, related_name="posts")
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def str(self):
        return f"title: {self.title} user_id: {self.user_id}"