# Generated by Django 5.0.7 on 2024-08-08 12:43

import bank_account.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_account', '0002_alter_bankaccount_iban'),
        ('person', '0004_alter_person_national_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankaccount',
            name='IBAN',
            field=models.CharField(validators=[bank_account.validators.validate_24_digits]),
        ),
        migrations.AlterField(
            model_name='bankaccount',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='accounts', to='person.person'),
        ),
    ]
