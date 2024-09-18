from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from yandexid import YandexID
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response

from .serializers import YandexAuthSerializer


UserModel = get_user_model()


class YandexAuthView(APIView):
    
    @extend_schema(request=YandexAuthSerializer, responses={200: TokenObtainPairSerializer})
    def post(self, request):    
        serializer = YandexAuthSerializer(data=request.data)
        if serializer.is_valid():
            token = serializer.data['ya_token']
        yandex_id = YandexID(token)
        user_info = yandex_id.get_user_info_json()
        user = UserModel.objects.filter(email=user_info.default_email).first()
        if user is None:
            user = UserModel.objects.create(
                email=user_info.default_email,
                birthday=user_info.birthday if user_info.birthday else None,
                first_name=user_info.first_name,
                last_name=user_info.last_name,
                password='dummy password',  
            )
            user.password = 'not hashed pass'
            user.save()

        refresh = RefreshToken.for_user(user)
        return Response({'access': str(refresh.access_token), 'refresh': str(refresh)})
