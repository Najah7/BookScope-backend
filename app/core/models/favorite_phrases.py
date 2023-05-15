from django.db import models



from django.conf import settings

class FavoritePhrase(models.Model):
    
    class Meta:
        db_table = 'favorite_phrases'
        app_label = "core"
        
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phrase = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)