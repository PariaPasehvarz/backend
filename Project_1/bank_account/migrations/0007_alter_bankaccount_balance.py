# Generated by Django 5.0.7 on 2024-08-10 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_account', '0006_alter_bankaccount_iban'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankaccount',
            name='balance',
            field=models.DecimalField(decimal_places=0, max_digits=25),
        ),
    ]
