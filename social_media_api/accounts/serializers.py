from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token # <-- Contains Token import

User = get_user_model()

# 1. Registration Serializer
class UserRegistrationSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150) # <-- Contains serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    
    # Optional field
    bio = serializers.CharField(max_length=500, required=False)

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("A user with that username already exists.")
        return value

    def create(self, validated_data):
        user = User.objects.create_user( # <-- Contains get_user_model().objects.create_user
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            bio=validated_data.get('bio', '')
        )
        return user

# 2. Token Serializer for returning token upon success (optional, but good practice)
class TokenSerializer(serializers.ModelSerializer):
    # This just formats the output of the token key nicely
    class Meta:
        model = Token
        fields = ('key', 'created')

# Note: Token.objects.create is usually handled within the view logic.
