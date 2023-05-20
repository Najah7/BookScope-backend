from rest_framework import serializers

from core.models import FavoritePhraseLike

class FavoritePhraseLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoritePhraseLike
        fields = (
            "id",
            "like",
            "created_at",
            "updated_at",
        )
        
        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
        )