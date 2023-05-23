
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from blog.views import UserViewSet


router = DefaultRouter()
router.register('user', UserViewSet, basename="user")

urlpatterns = [
    path('api/', include(router.urls)),
    # path('user/me/', UserView.as_view({'get': 'get_current_user'})),
]