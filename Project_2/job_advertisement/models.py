from django.db import models
from model_utils.models import TimeStampedModel
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

class BrachTypeChoices(models.TextChoices):
    MARKETING_ROLES = 'marketing roles', 'marketing roles'
    BUSINESS_DEVELOPMENT_ROLES  = 'business development roles', 'business development roles'
    DESIGN_ROLES = 'design roles', 'design roles',
    ANALYTICS_ROLES = 'analytics roles', 'analytics roles',
    ADMINISTRATIVE_ROLES = 'administrative roles', 'administrative roles',
    IT_ROLES = 'IT roles', 'IT roles',
    FINANCE_ROLES = 'finance roles', 'finance roles',
    HEALTHCARE_ROLES = 'healthcare roles', 'healthcare roles',
    EDUCATION_ROLES = 'education roles', 'education roles',
    ENGINEERING_ROLES = 'engineering roles', 'engineering roles'


class JobAdvertisement(TimeStampedModel):
    title = models.CharField(max_length = 63, default = "")
    owner = models.ForeignKey(to = User, on_delete = models.CASCADE, related_name = 'advertisements')
    applicants = models.ManyToManyField(to = User, related_name = 'applicants',default = None)
    image = models.ImageField(default = None, null = True, blank = True)
    expire_time = models.DateTimeField()
    job_category = models.CharField(max_length = 50, choices = BrachTypeChoices.choices, default = BrachTypeChoices.MARKETING_ROLES)
    salary = models.PositiveIntegerField() 
    insurance = models.BooleanField(default = False)
    working_time = models.PositiveBigIntegerField(
        default = 8, validators = [MinValueValidator(1), MaxValueValidator(24)])

    def __str__(self):
        return self.title 