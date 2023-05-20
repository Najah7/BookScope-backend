from rest_framework import serializers

from core.models import Post
from core.serializers import (
    UserSerializer,
    PostCommentSerializer,
    PostLikeSerializer,
    PostTagSerializer,
)

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    comments = PostCommentSerializer(many=True)
    likes = PostLikeSerializer(many=True)
    tags = PostTagSerializer(many=True)
    
    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "content",
            "author",
            "comments",
            "likes",
            "tags",
            "read_book",
            "created_at",
            "updated_at",
        )
        
        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
        )