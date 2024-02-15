from django.contrib import admin
from django.contrib.auth.models import Group, User


from .models import Person


class PersonAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'last_name', 'first_name', 'patronymic',
        'company', 'work_phone', 'personal_phone')
    search_fields = ('last_name', 'first_name', 'patronymic',
                     'company', 'work_phone', 'personal_phone',)
    list_filter = ('company',)
    empty_value_display = '-пусто-'


admin.site.register(Person, PersonAdmin)
admin.site.unregister(Group)
admin.site.unregister(User)
