from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели User.
    """
    class Meta:
        model = User
        # fields = "__all__"
        fields = ('id', 'email', 'password', 'tg_chat_id')
        extra_kwargs = {'password': {'write_only': True}}


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Сериализатор для обработки запросов на получение токена.
    """
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Добавление пользовательских полей в токен
        token['username'] = user.username
        token['email'] = user.email

        return token



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def my_protected_view(request):
    # Ваш код представления
    return Response({'message': 'Авторизовано!'})
