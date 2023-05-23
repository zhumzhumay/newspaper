from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.viewsets import ModelViewSet

from blog.models import User
from blog.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    # filter_backends=[DjangoFilterBackend]
    # filterset_fields = ['title', 'text']

    # def get_permissions(self):
    #     if self.action in ['list', 'retrieve']:
    #         self.permission_classes = [AllowAny]
    #     else:
    #         self.permission_classes = [IsAdminUser]