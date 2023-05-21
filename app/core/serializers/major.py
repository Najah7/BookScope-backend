from rest_framework import serializers

from core.models import Major

class MajorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Major
        fields = (
            "id",
            "name",
        )
        
        read_only_fields = (
            "id",
        )