from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView

from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema

from users.models import User
from users.serializers import UserSerializer


@method_decorator(
    name="list",
    decorator=swagger_auto_schema(
        operation_description="Контроллер для получения списка всех пользователей"
    ),
)
@method_decorator(
    name="retrieve",
    decorator=swagger_auto_schema(
        operation_description="Контроллер для получения конкретного пользователя"
    ),
)
@method_decorator(
    name="create",
    decorator=swagger_auto_schema(
        operation_description="Контроллер для создания пользователя"
    ),
)
@method_decorator(
    name="update",
    decorator=swagger_auto_schema(
        operation_description="Контроллер для обновления информации о пользователе"
    ),
)
@method_decorator(
    name="partial_update",
    decorator=swagger_auto_schema(
        operation_description="Контроллер для частичного изменения информации о пользователе"
    ),
)
@method_decorator(
    name="destroy",
    decorator=swagger_auto_schema(
        operation_description="Контроллер для удаления пользователя"
    ),
)
class UserViewSet(ModelViewSet):
    """
    Представление для модели User CRUD.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserCreateApiView(CreateAPIView):
    """
    Создание пользователя
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()
