from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from user.models import Users
from user.serializers import UsersSerializer, UsersDetailSerializer


class UserViewSet(viewsets.ModelViewSet):

    serializer_class = UsersSerializer
    retrieve_serializer_class = UsersDetailSerializer
    list_serializer_class = UsersDetailSerializer
    filter_backends = None
    queryset = Users.objects.all()
    permission_classes = [AllowAny]
