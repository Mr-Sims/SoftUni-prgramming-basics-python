from django.core.exceptions import ValidationError


def validate_dot(value):
    if '.' in value:
        raise ValidationError('\'.\' is present in value')