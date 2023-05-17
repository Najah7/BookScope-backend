from django.db import models

from core.models import Post

class PostTag(models.Model):
    class Meta:
        db_table = "post_tags"
        app_label = "core"

    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_tags")
    tag = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def str(self):
        return f"tag: {self.tag} post_id: {self.post_id}"