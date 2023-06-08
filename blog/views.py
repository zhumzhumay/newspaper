from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.views import TokenObtainSlidingView, TokenRefreshSlidingView

from blog.models import User, Post
from blog.permissions import IsEditor, IsSuperAdmin, IsReader
from blog.serializers import UserSerializer, TokenObtainPairSerializer, TokenRefreshSerializer, PostSerializer


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


class EditorView(ListAPIView):
    permission_classes = [IsEditor | IsSuperAdmin]

    def get(self, request, *args, **kwargs):
        return Response(data={'success': 'You are a editor'}, status=status.HTTP_200_OK)


class ReaderView(ListAPIView):
    permission_classes = [IsReader | IsSuperAdmin | IsEditor]

    def get(self, request, *args, **kwargs):
        return Response(data={'success': 'You are a reader'}, status=status.HTTP_200_OK)


class TokenObtainPairView(TokenObtainSlidingView):
    permission_classes = [AllowAny]
    serializer_class = TokenObtainPairSerializer


class TokenRefreshView(TokenRefreshSlidingView):
    permission_classes = [AllowAny]
    serializer_class = TokenRefreshSerializer

class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

def index(request):
    # ls = Post.NEWS_TYPES
    return render(request, 'index.html')