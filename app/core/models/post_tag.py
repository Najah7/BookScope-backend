from django.db import models

from core import models as CoreModels


class PostTag(models.Model):
    class Meta:
        db_table = "post_tags"
        app_label = "core"

    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def str(self):
        return f"tag: {self.tag} post_id: {self.post_id}"
