from rest_framework import serializers
from app.models import User, Post

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    password = serializers.CharField()
    bio = serializers.CharField()

    def create(self, validated_data):
        return User.objects.create(**validated_data)
    
class UserLoginSerializers(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
    title = serializers.CharField()
    description = serializers.CharField()
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

