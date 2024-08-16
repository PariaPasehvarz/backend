from django.db import models
from .validators import validate_ten_digits

class Person(models.Model):
    
    first_name = models.CharField(max_length = 63)
    last_name = models.CharField(max_length = 63)
    national_code = models.PositiveBigIntegerField(validators = [validate_ten_digits])