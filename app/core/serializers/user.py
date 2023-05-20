from rest_framework import serializers

from core.models import CustomUser
from core.serializers import PostLikeSerializer, PostCommentSerializer

class UserSerializer(serializers.ModelSerializer):
    post_like = PostLikeSerializer(many=True)
    post_comment = PostCommentSerializer(many=True)
    class Meta:
        model = CustomUser
        fields = (
            "id",
            "post_like",
            "post_comment",
            "email",
            "user_name",
            "password",
            "self_introduction",
            "icon",
            "twitter",
            "instagram",
            "facebook",
            "youtube",
            "created_at",
            "updated_at",
        )
        
        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
        )