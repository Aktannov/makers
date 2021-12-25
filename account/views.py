from django.core.mail import send_mail
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.viewsets import ModelViewSet

from account.serializer import RegisterSerializer, LoginSerializer, ActivationSerializer, ForgotPasswordSerializer, \
    ForgotPasswordFinalSerializer


class RegistrationView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.create()
            message = f'Вы зарегались' \
                      f'Вы получили код активации'
            return Response(message, status=201)


class ActivationView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        data = request.data
        serializer = ActivationSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.activate()
            return Response('Ваш аккаунт активирован')


class LoginView(ObtainAuthToken):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):

        user = request.user
        Token.objects.filter(user=user).delete()
        return Response('Вы успешно разлогинились')

class ForgotPasswordView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data
        serializer = ForgotPasswordSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.send_code()
        return Response('Вам отправлено письмо для восстановления пароля')


class ForgotPasswordFinalView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data
        serializer = ForgotPasswordFinalSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.set_pass()
        return Response('Пароль успешно обнавлен')
