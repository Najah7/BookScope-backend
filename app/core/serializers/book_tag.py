from rest_framework import serializers

from core.models import BookTag

class BookTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookTag
        fields = (
            "id",
            "name",
        )