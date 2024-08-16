#Query 4
#Get 5 bank accounts with highest balance.

import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Project_1.settings')
django.setup()

from bank_account.models import BankAccount

accounts_with_highest_balance = BankAccount.objects.all().order_by('-balance')[:5]

print('5 Bank Accounts with highest balance:\n')
i = 1

for account in accounts_with_highest_balance:
    
    print('Account ' + str(i))
    print('Owner First Name: ' +  account.owner.first_name + '\n' +
        'Owner Last Name: ' + account.owner.last_name + '\n' + 
        'Owner National Code: ' + str(account.owner.national_code) + '\n' +
        'Account IBAN: ' + str(account.IBAN) + '\n' + 
        'Account Balance: ' + str(account.balance) + '\n')
    i += 1