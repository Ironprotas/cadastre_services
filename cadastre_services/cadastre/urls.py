from .views import query, ping
from django.urls import path

urlpatterns = [
    path('query/', query, name='query'),
    path('ping/', ping, name='ping'),

]
