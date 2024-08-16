#Query 2
#Get a list of all accounts' owners with their name and  balance.
#I assumed we want first name and last simoltaneously.

import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Project_1.settings')
django.setup()

from bank_account.models import BankAccount

account_with_owner = BankAccount.objects.select_related('owner')

print('List of all accounts with their owner name and balance\n')

i = 1
for account in account_with_owner:
    
    print('Account ' + str(i))
    print("Owner First Name: " + account.owner.first_name + '\n'
           + "Owner Last Name: " + account.owner.last_name + '\n' 
           + "Account Balance: " + str(account.balance) + '\n')
    i+= 1
