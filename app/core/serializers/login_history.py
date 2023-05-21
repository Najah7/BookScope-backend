from rest_framework import serializers

from core.models import LoginHistory
from core.serializers.user import UserSerializer

class LoginHistorySerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = LoginHistory
        fields = (
            "id",
            "user",
            "created_at",
            "updated_at",
        )
        
        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
        )