from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import PersonViewSet

app_name = 'api'


router = DefaultRouter()
router.register(r'contacts', PersonViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
]
