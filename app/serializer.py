from rest_framework import serializers
from app.models import User

class UserSerialzers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    email = serializers.EmailField()
    first_name = serializers.CharField