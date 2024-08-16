from django.core.exceptions import ValidationError

def validate_ten_digits(value):

    if len(str(value)) != 10:
        raise ValidationError('This field must be exactly 10 digits long')