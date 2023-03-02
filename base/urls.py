from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('1/2/3/4/5/6/7/8/9/0', views.home2, name="teste"),
]
