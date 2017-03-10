from rest_framework import permissions


class UserPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        if view.action in ['retrieve', 'update']:
            return request.user.is_authenticated()
        elif view.action == 'create':
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if view.action == 'retrieve':
            return request.user.is_authenticated() and (obj == request.user or request.user.is_staff)
        elif view.action == 'update':
            return request.user.is_authenticated() and (obj == request.user)
        else:
            return False
