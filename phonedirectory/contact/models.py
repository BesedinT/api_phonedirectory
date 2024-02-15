from django.core.exceptions import ValidationError
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Person(models.Model):
    last_name = models.CharField(
        'Фамилия',
        max_length=50,
        blank=True,
    )
    first_name = models.CharField(
        'Имя',
        max_length=50,
        blank=False,
    )
    patronymic = models.CharField(
        'Отчество',
        max_length=50,
        blank=True,
    )
    company = models.CharField(
        'Название оранизации',
        max_length=50,
        blank=True,
    )
    work_phone = PhoneNumberField(
        'Рабочий телефон',
        null=False,
        blank=False,
    )
    personal_phone = PhoneNumberField(
        'Личный телефон',
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
        ordering = ('last_name', 'first_name', 'patronymic')

    def __str__(self):
        return self.first_name
