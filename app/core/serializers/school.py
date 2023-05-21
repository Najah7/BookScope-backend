from rest_framework import serializers

from core.models import School

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = (
            "id",
            "name",
        )
        
        read_only_fields = (
            "id",
        )