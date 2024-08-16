#Query 5
#Function to wire some money from an account to another one.

import django
import os

from django.db.models import F

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Project_1.settings')
django.setup()

from bank_account.models import BankAccount

def wiring(source_IBAN, destination_IBAN, money_amount):

    BankAccount.objects.filter(IBAN = source_IBAN).update(balance = F('balance') - money_amount)
    BankAccount.objects.filter(IBAN = destination_IBAN).update(balance = F('balance') + money_amount)

#Test!    
wiring(BankAccount.objects.first().IBAN, BankAccount.objects.last().IBAN, 36)