#Query 3
#Get bank account with highest balance.

import django
import os

from django.db.models import Max

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Project_1.settings')
django.setup()

from bank_account.models import BankAccount

max_value = BankAccount.objects.aggregate(Max('balance'))['balance__max']
account_with_highest_balance = BankAccount.objects.get(balance = max_value)

print('Bank Account with highest balance:\n')
print('Owner First Name: ' +  account_with_highest_balance.owner.first_name + '\n' +
      'Owner Last Name: ' + account_with_highest_balance.owner.last_name + '\n' + 
      'Owner National Code: ' + str(account_with_highest_balance.owner.national_code) + '\n' +
      'Account IBAN: ' + str(account_with_highest_balance.IBAN) + '\n' + 
      'Account Balance: ' + str(account_with_highest_balance.balance))