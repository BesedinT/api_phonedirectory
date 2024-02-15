# Generated by Django 4.2.10 on 2024-02-11 19:27

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(blank=True, max_length=50, verbose_name='Фамилия')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('patronymic', models.CharField(blank=True, max_length=50, verbose_name='Отчество')),
                ('company', models.CharField(blank=True, max_length=50, verbose_name='Название оранизации')),
                ('work_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='Рабочий телефон')),
                ('personal_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='Личный телефон')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
                'ordering': ('last_name', 'first_name', 'patronymic'),
            },
        ),
        migrations.AddConstraint(
            model_name='person',
            constraint=models.CheckConstraint(check=models.Q(models.Q(('work_phone__isnull', False), ('personal_phone__isnull', True)), models.Q(('work_phone__isnull', True), ('personal_phone__isnull', False)), models.Q(('work_phone__isnull', True), ('personal_phone__isnull', True)), _connector='OR'), name='Enter_at_least_one_number'),
        ),
    ]
