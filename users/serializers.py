from rest_framework import serializers as s

from users.models import User


class UserSerializer(s.Serializer):
    class Meta:
        model = User
        fields = '__all__'
