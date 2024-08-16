#Query 7
#Bank Accounts which owner national code is larger than Balance

import django
import os
from django.db.models import F

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Project_1.settings')
django.setup()

from bank_account.models import BankAccount

accounts_list = BankAccount.objects.filter(owner__national_code__gt = F("balance"))

print('Bank Accounts which owner national code is larger than Balance\n')

i = 1
for account in accounts_list:
    
    print('Account ' + str(i))
    print('Owner First Name: ' +  account.owner.first_name + '\n' +
        'Owner Last Name: ' + account.owner.last_name + '\n' + 
        'Owner National Code: ' + str(account.owner.national_code) + '\n' +
        'Account IBAN: ' + str(account.IBAN) + '\n' + 
        'Account Balance: ' + str(account.balance) + '\n')
    i += 1