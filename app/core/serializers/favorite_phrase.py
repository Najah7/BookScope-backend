from rest_framework import serializers

from core.models import FavoritePhrase
from core.serializers.user import UserSerializer

class FavoritePhraseSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = FavoritePhrase
        fields = (
            "id",
            "user",
            "phrase",
            "created_at",
            "updated_at",
        )
        
        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
        )