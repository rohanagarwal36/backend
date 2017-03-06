from django.http import HttpResponse


def get_user_not_found_response():
    response = HttpResponse("User doesn't exist")
    response.status_code = 401
    return response


def get_unauthorized_operation_response():
    response = HttpResponse("Operation not allowed: Unauthorized user")
    response.status_code = 401
    return response


def is_authorized(request, id):
    if request.user.id != int(id):
        return False
    return True


def is_admin(request):
    if request.user.is_superuser:
        return True
    return False
