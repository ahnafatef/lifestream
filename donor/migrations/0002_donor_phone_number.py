# Generated by Django 2.1 on 2019-09-08 12:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='donor',
            name='phone_number',
            field=models.CharField(blank=True, max_length=11, validators=[django.core.validators.RegexValidator(message='Phone number must be of the form: 01XXXXXXXXX', regex='^[0]{1}[\\d]{10}')]),
        ),
    ]