from django.urls import include, path
from rest_framework.routers import DefaultRouter

from blog.views import UserViewSet, EditorView, ReaderView, TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register('user', UserViewSet, basename="user")

urlpatterns = [
    path('api/', include(router.urls)),
    path('editor/get', EditorView.as_view()),
    path('reader/', ReaderView.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]
