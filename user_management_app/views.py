from django.contrib.auth.hashers import check_password
from django.http.response import HttpResponse
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from user_management_app import utils
from user_management_app.mixins import UserMixin
from user_management_app.models import User
from user_management_app.serializers import LoginSerializer, TokenSerializer


class UserAPI(UserMixin, viewsets.ModelViewSet):
    pass


class Login(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        email = serializer.initial_data['email']
        password = serializer.initial_data['password']
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return utils.get_user_not_found_response()

        encoded_password = user.password

        if not check_password(password, encoded_password):
            response = HttpResponse("Incorrect password")
            response.status_code = 401
            return response

        token, created = Token.objects.get_or_create(user=user)

        auth_details_serializer = TokenSerializer(token)
        return Response(auth_details_serializer.data, status=status.HTTP_200_OK)


class Logout(APIView):
    def get(self, request):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
