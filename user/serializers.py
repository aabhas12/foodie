from django.core.exceptions import ObjectDoesNotExist
from oauthlib.oauth2.rfc6749.tokens import random_token_generator
from rest_framework import serializers
from user.models import Users
from oauth2_provider.models import RefreshToken, AccessToken, Application
from datetime import datetime, timedelta
from foodie.settings import OAUTH2_PROVIDER


class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ('firstname', 'lastname', 'username', 'avatar')


class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ('email', 'username', 'password', 'firstname', 'lastname')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        instance = super().create(validated_data)
        instance.set_password(password)
        instance.save()

        expire_seconds = OAUTH2_PROVIDER['ACCESS_TOKEN_EXPIRE_SECONDS']
        scopes = OAUTH2_PROVIDER['SCOPES']
        application = Application.objects.get(name="GeniusSis")
        expires = datetime.now() + timedelta(seconds=expire_seconds)
        access_token = AccessToken.objects.create(
            user=instance,
            application=application,
            token=random_token_generator(self.context['request']),
            expires=expires,
            scope=scopes)

        refresh_token = RefreshToken.objects.create(
            user=instance,
            token=random_token_generator(self.context['request']),
            access_token=access_token,
            application=application)
        return instance

    def update(self, instance, validated_data):
        pass


class UsersDetailSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()

    class Meta:
        model = Users
        fields = ('email', 'username', 'password', 'firstname', 'lastname', 'token')

    def get_token(self, user):
        expire_seconds = OAUTH2_PROVIDER['ACCESS_TOKEN_EXPIRE_SECONDS']
        scopes = OAUTH2_PROVIDER['SCOPES']
        application = Application.objects.get(name="GeniusSis")
        expires = datetime.now() + timedelta(seconds=expire_seconds)
        try:
            access_token = AccessToken.objects.get(
                user=user)

            refresh_token = RefreshToken.objects.get(
                user=user)

            token = {
                'access_token': access_token.token,
                'token_type': 'Bearer',
                'expires_in': expire_seconds,
                'refresh_token': refresh_token.token,
                'scope': scopes}

        except ObjectDoesNotExist:
            token = None

        return token
