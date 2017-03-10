from rest_framework.exceptions import ValidationError

from user_management_app.constants import AGE_ERROR, MIN_AGE


def validate_adult(value):
    if value < MIN_AGE:
        raise ValidationError(AGE_ERROR)
