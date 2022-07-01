from django.urls import path
from .views import beep_in_5
urlpatterns = [
    path("",beep_in_5)
]
