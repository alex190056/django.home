from django.urls import path
from catalog.apps import AppConfig
from catalog.views import home, contacts

app_name = AppConfig

urlpatterns = [
    path('contacts/', contacts),
    path('home/', home)
]
