#Query 8
#Bank Accounts which their balance is less than 1 millions or bigger than 2 millions
#I had to decrease number of records to 1 million due to the limit of recources
#I developed this code on virtual machine with only 3 cores.

import django
import os
import time
from django.db.models import Q

start_time = time.time()

MIN_VALUE = 2000000
MAX_VALUE = 1000000

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Project_1.settings')
django.setup()

from bank_account.models import BankAccount

accounts_list = BankAccount.objects.exclude(Q(balance__gt = MIN_VALUE) & Q(balance__lt = MAX_VALUE))

print('Bank Accounts which their balance is less than 1 millions or bigger than 2 millions')

print('Execution time: %s\n'%(time.time() - start_time))