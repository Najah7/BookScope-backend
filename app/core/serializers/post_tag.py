from rest_framework import serializers

from core.models import PostTag

class PostTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostTag
        fields = (
            "id",
            "name",
        )
        
        read_only_fields = (
            "id",
        )