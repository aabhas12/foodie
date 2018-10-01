from rest_framework import serializers
from user.models import Users


class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ('first_name', 'last_name', 'username', 'avatar')
