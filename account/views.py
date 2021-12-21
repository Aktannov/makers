from rest_framework.response import Response
from rest_framework.views import APIView

from account.serializer import RegisterSerializer


class RegistrationView(APIView):
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.create()
            message = f'Вы успешно зарегестрировались\nВам отправлено письмо активации'
            return Response(message, status=201)
