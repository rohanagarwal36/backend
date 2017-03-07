from django.contrib.auth.hashers import make_password
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin

from user_management_app.models import User
from user_management_app.permissions import UserPermissions
from user_management_app.serializers import UserSerializer


class UserMixin(CreateModelMixin, UpdateModelMixin):
    model = User
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [UserPermissions]

    def perform_create(self, serializer):
        hashed_password = make_password(serializer.validated_data['password'])
        serializer.validated_data['password'] = hashed_password
        super(UserMixin, self).perform_create(serializer)

    def perform_update(self, serializer):
        hashed_password = make_password(serializer.validated_data['password'])
        serializer.validated_data['password'] = hashed_password
        super(UserMixin, self).perform_update(serializer)