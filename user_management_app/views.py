from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from user_management_app.models import User
from user_management_app.permissions import UserPermissions
from user_management_app.serializers import LoginSerializer, TokenSerializer, UserSerializer


class UserAPIViewSet(ModelViewSet):
    model = User
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [UserPermissions]


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data['email']
            user = User.objects.get(email=email)
            user.auth_token.delete()
            token = Token.objects.create(user=user)
            auth_details_serializer = TokenSerializer(token)
            return Response(auth_details_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Logout(DestroyAPIView):
    def delete(self, request, *args, **kwargs):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
