from django.shortcuts import render, redirect
from django.utils import timezone
from rest_framework import status, mixins
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework_simplejwt.views import TokenObtainSlidingView, TokenRefreshSlidingView

from blog.forms import PostForm, LoginForm
from blog.models import User, Post, Sessions
from blog.permissions import IsEditor, IsSuperAdmin, IsReader
from blog.serializers import UserSerializer, TokenObtainPairSerializer, TokenRefreshSerializer, PostSerializer

from django.contrib.auth import authenticate, login


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

# class PostViewSet (mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin,
#                    GenericViewSet):
class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

# class PostCreateView(mixins.CreateModelMixin, GenericViewSet):
#     permission_classes = [IsEditor | IsSuperAdmin]
#     def get(self, request, *args, **kwargs):
#         return Response(data={'success': 'You posted it'}, status=status.HTTP_200_OK)

def index(request):
    # ls = Post.NEWS_TYPES
    return render(request, 'index.html')

def error(request):
    return render(request, 'error.html')

def signin(request):
    if request.method == "POST":
        
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('post_add')
        else:
        # Return an 'invalid login' error message.
            return redirect('error')
    else:
        form = LoginForm()
    
        # Redirect to a success page.
        
        
    return render(request, 'signin.html', {'form': form})

def post_form(request):

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            
            post = form.save(commit=False)
            post.user = request.user
            post.post_date = timezone.now()
            post.save()
            # img_obj = form.instance
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'post_add.html', {'form': form})

# def login_form(request):
#     if request.method == "POST":
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             # post = form.save(commit=False)
#             # if Sessions.objects.get(id=User.objects.get(username=post.username).id):
#             #     Sessions.objects.get(id=User.objects.get(username=post.username).id).delete()
#             # post.date = timezone.now()
#             # post.token =
#             # post.save()
#             return redirect('index')
#     else:
#         form = LoginForm()
#     return render(request, 'signin.html', {'form': form})