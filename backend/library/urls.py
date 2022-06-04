from django.urls import path
from .views import UserViewSet

app_name = 'library'

urlpatterns = [
    path('', UserViewSet.as_view({'get': 'list'}))
]
