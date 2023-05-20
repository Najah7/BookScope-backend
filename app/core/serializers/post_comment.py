from rest_framework import serializers

from core.models import PostComment

class PostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostComment
        fields = (
            "id",
            "comment",
            "created_at",
            "updated_at",
        )
        
        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
        )