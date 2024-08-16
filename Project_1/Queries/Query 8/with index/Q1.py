#Query 1
#Create 1000000 random record for bank_account

NUM_RECORD = 1000000
NATIONAL_CODE_LENGTH = 10
IBAN_LENGTH = 24
MAXIMUM_POSSIBLE_ACCOUNT = 30
MAX_NAME_LENGTH = 63
BATCH_SIZE = 5000
MAXIMUM_BALANCE_VALUE = 10**24

import random
import string
import django
import os
import math
from django.db import transaction

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Project_1.settings')
django.setup()

from person.models import Person
from bank_account.models import BankAccount

def generate_random_name(length):

    return ''.join(random.choice(string.ascii_lowercase) for i in range(length))

def generate_random_code(length, num_people):

    unique_numbers = set()
    start = 10**(length-1)-1
    end = 10**length-1

    while len(unique_numbers) < num_people:
        number = random.randint(start, end)
        unique_numbers.add(number)

    return list(unique_numbers)

def select_eligible_person():

    person = random.choice(persons)
    while BankAccount.objects.filter(owner = person).count() >= MAXIMUM_POSSIBLE_ACCOUNT:
        person = random.choice(persons)
    return person

def generate_random_person(national_code):

    first_name_length = random.randint(1, MAX_NAME_LENGTH)
    last_name_length = random.randint(1, MAX_NAME_LENGTH)
    _first_name = generate_random_name(first_name_length)
    _last_name = generate_random_name(last_name_length)
    _national_code = national_code

    return Person(first_name = _first_name, last_name = _last_name, national_code = _national_code)

def generate_random_account(_owner, _IBAN):

    _balance = random.randint(0, MAXIMUM_BALANCE_VALUE)
    return BankAccount(owner = _owner, IBAN = _IBAN, balance = _balance)

min_num_people = math.ceil(NUM_RECORD/MAXIMUM_POSSIBLE_ACCOUNT)
num_people = random.randint(min_num_people, NUM_RECORD)

persons = []
national_code_list = generate_random_code(NATIONAL_CODE_LENGTH, num_people)
i = 0
for _ in range(num_people):
    national_code = national_code_list[i]
    person = generate_random_person(national_code)
    persons.append(person)
    i += 1

with transaction.atomic():
    for i in range(0, len(persons), BATCH_SIZE):
        Person.objects.bulk_create(persons[i: i + BATCH_SIZE])

bank_accounts = []
IBAN_list = generate_random_code(IBAN_LENGTH, NUM_RECORD)

i = 0
for person in persons:
    owner = person
    IBAN = IBAN_list[i]
    account = generate_random_account(owner, IBAN)
    bank_accounts.append(account)
    i += 1

remaining_accounts = NUM_RECORD - num_people

while remaining_accounts > 0:
    owner = select_eligible_person()
    IBAN = IBAN_list[i]
    account = generate_random_account(owner, IBAN)
    bank_accounts.append(account)
    remaining_accounts -= 1
    i += 1

with transaction.atomic():
    for i in range(0, len(bank_accounts), BATCH_SIZE):
        BankAccount.objects.bulk_create(bank_accounts[i: i + BATCH_SIZE])
