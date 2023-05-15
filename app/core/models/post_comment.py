from django.db import models

from core.models import Post
from django.conf import settings

class PostComment(models.Model):
    
    class Meta:
        db_table = 'post_comments'
        app_label = "core"
    
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)