from django.urls import path, include
from . import views


urlpatterns = [
    path('Printer', views.testing_scripts, name="testing_scripts"),
    path('Contador', views.contador, name="contador"),
    path('FizzBuzz', views.fizzbuzz, name="fizzbuzz"),
]
