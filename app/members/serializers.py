from django.contrib.auth import get_user_model
from rest_framework import serializers

from snippets.models import Snippet

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']
        depth = 1


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def validate_email(self, value):
        check_email_duplicate = User.objects.filter(email=value).exists()
        if check_email_duplicate is True:
            raise serializers.ValidationError('이미 존재하는 이메일입니다')
        return value
