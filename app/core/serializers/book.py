from rest_framework import serializers

from core.models import Book
from core.serializers import (
    PublisherSerializer,
    AuthorSerializer,
    BookTagSerializer,
    
)

class BookSerializer(serializers.ModelSerializer):
    
    authors = AuthorSerializer(many=True)
    publishers = PublisherSerializer(many=True)
    tags = BookTagSerializer(many=True)
    class Meta:
        model = Book
        fields = (
            "id",
            "title",
            "isbn",
            "price",
            "image_url",
            "authors",
            "publishers",
            "tags",
        )