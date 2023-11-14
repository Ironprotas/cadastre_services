from django.urls import path
from .views import history_by_cadastre

urlpatterns = [
    path('history/<str:cadastre_number>/', history_by_cadastre, name='history_by_cadastre'),
]