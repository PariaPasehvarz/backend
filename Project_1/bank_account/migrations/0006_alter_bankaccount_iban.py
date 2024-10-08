# Generated by Django 5.0.7 on 2024-08-10 12:13

import bank_account.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_account', '0005_alter_bankaccount_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankaccount',
            name='IBAN',
            field=models.DecimalField(decimal_places=0, max_digits=24, validators=[bank_account.validators.validate_24_digits]),
        ),
    ]
