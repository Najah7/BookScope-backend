from rest_framework import serializers

from core.models import ReadBook
from core.serializers.book import BookSerializer

class ReadBookSerializer(serializers.ModelSerializer):
    book = BookSerializer()
    class Meta:
        model = ReadBook
        fields = (
            "id",
            "user",
            "book",
            "read_at",
        )
        
        read_only_fields = (
            "id",
        )