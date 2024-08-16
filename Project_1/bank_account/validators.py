from django.core.exceptions import ValidationError

def validate_24_digits(value):

    if len(str(value)) != 24:
        raise ValidationError('This field must be exactly 10 digits long')