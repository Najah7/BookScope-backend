from django.db import models

from core.models import FavoritePhrase

class FavoritePhraseLike(models.Model):
    
    class Meta:
        db_table = 'favorite_phrase_likes'
        app_label = "core"
    
    favorite_phrase_id = models.ForeignKey(FavoritePhrase, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)