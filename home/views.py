# pylint: disable=missing-module-docstring

from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class HomeView(LoginRequiredMixin, TemplateView):  
    template_name = "home/home.html"
    login_url = "/admin/"
    
