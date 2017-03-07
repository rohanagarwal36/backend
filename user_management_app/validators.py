from rest_framework.exceptions import ValidationError


def validate_adult(value):
    if value < 18:
        raise ValidationError('Age should be greater than 18 years')
