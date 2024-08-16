#Query 9
#Calculate sum of balance for each person in bank(use only one query)

import django
import os
from django.db.models import Sum

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Project_1.settings')
django.setup()

from person.models import Person

people_with_total_balance = Person.objects.annotate(total_balance = Sum("accounts__balance"))

print('Calculate sum of balance for each person in bank\n')

i = 1
for person in people_with_total_balance:
    
    print('Person ' + str(i))
    print('Owner first name: ' + person.first_name + '\n'
          + 'Owner last name: ' + person.last_name + '\n'
          + 'Owner national code: ' + str(person.national_code) + '\n'
          'Total Balance: ' +  str(person.total_balance) + '\n')
    i += 1