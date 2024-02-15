# Generated by Django 4.2.10 on 2024-02-15 20:04

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_alter_person_work_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='work_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='Рабочий телефон'),
        ),
    ]
