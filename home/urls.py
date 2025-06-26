# pylint: disable=missing-module-docstring
from django.urls import path
from home.views import HomeView

APP_NAME = "home"

urlpatterns = [
    path("",HomeView.as_view(), name="home"),
]
