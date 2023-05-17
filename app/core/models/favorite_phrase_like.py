from django.db import models
from django.conf import settings

from core.models import FavoritePhrase

class FavoritePhraseLike(models.Model):
    class Meta:
        db_table = "favorite_phrase_likes"
        app_label = "core"

    favorite_phrase_id = models.ForeignKey(FavoritePhrase, on_delete=models.CASCADE, related_name="favorite_phrase_likes")
    # HACK: 一時的にデフォルト値を設定
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"favorite_phrase_id: {self.favorite_phrase_id} user_id: {self.user_id}"
