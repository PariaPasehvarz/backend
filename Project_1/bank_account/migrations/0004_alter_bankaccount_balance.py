# Generated by Django 5.0.7 on 2024-08-09 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_account', '0003_alter_bankaccount_iban_alter_bankaccount_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankaccount',
            name='balance',
            field=models.CharField(),
        ),
    ]
