# cadastre/urls.py

from .views import query, result, ping
from django.urls import path

urlpatterns = [
    path('query/', query, name='query'),
    path('result/', result, name='result'),
    path('ping/', ping, name='ping'),

]
