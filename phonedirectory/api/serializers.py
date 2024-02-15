from rest_framework import serializers

from contact.models import Person


class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = (
            'last_name',
            'first_name',
            'patronymic',
            'company', 'work_phone',
            'personal_phone'
        )
