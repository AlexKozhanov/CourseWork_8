from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import (
    # TokenObtainPairView,
    TokenRefreshView)
from users.apps import UsersConfig
from users.views import (
    UserViewSet,
    UserCreateApiView,
    MyTokenObtainPairView)

app_name = UsersConfig.name

router = SimpleRouter()
router.register(r"", UserViewSet, basename="users")

urlpatterns = [
    path(
        'login/',
        MyTokenObtainPairView.as_view(permission_classes=(AllowAny,)),
        name='login'
    ),
    path(
        'token/refresh/',
        TokenRefreshView.as_view(permission_classes=(AllowAny,)),
        name='token_refresh'
    ),
    path("register/", UserCreateApiView.as_view(), name="register"),
]

urlpatterns += router.urls
