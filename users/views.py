from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth import get_user_model


from .serializers import UserSerialiser


UserModel = get_user_model()

class CreateUserView(CreateAPIView):
    model = UserModel
    serializer_class = UserSerialiser


class RetrieveUpdateDeleteUserView(RetrieveUpdateDestroyAPIView):
    model = UserModel
    serializer_class = UserSerialiser
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
