from django.urls import include, path
from rest_framework.routers import DefaultRouter

from blog.views import UserViewSet, EditorView, ReaderView, TokenObtainPairView, TokenRefreshView, index, PostViewSet, signin

from django.conf.urls.static import static
from django.conf import settings

router = DefaultRouter()
router.register('user', UserViewSet, basename="user")
router.register('post', PostViewSet, basename='post')

urlpatterns = [
    path('api/', include(router.urls)),
    path('', index, name='index'),
    path('signin/', signin, name='signin'),
    path('editor/get/', EditorView.as_view()),
    path('reader/get/', ReaderView.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
