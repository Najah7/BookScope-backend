from django.db import models

from django.conf import settings


class Rank(models.Model):
    class Meta:
        db_table = "rank"
        app_label = "core"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="rank"
    )
    name = models.CharField(max_length=200)
    rank_level = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def str(self):
        return f"name: {self.name} user_id: {self.user_id}"
