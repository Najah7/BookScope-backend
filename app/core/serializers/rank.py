from rest_framework import serializers

from core.models import Rank

class RankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rank
        fields = (
            "id",
            "name",
        )
        
        read_only_fields = (
            "id",
        )