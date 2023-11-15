from .views import result
from django.urls import path

urlpatterns = [
    path('result/', result, name='result'),
]
