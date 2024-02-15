from rest_framework import filters, viewsets
from rest_framework.pagination import LimitOffsetPagination

from .serializers import PersonSerializer
from contact.models import Person


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = (
        'last_name',
        'first_name',
        'patronymic',
        'company',
        'work_phone',
        'personal_phone'
        )
