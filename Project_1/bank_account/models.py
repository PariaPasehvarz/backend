from django.db import models
from .validators import validate_24_digits

class BankAccount(models.Model):
    
    owner = models.ForeignKey(
        to = 'person.Person', 
        on_delete = models.CASCADE, 
        null = True,
        related_name = 'accounts')
    IBAN = models.DecimalField(validators = [validate_24_digits], max_digits = 24, decimal_places = 0)
    balance = models.DecimalField(max_digits = 25, decimal_places = 0, db_index = True)

    def charge(self, count):
        self.count += count
        self.save()

    @property
    def sample_property(self):
        return f'{self.ISBN}|{self.publish_date}'