from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth import logout as auth_logout

# Create your views here.

class HomeView(TemplateView):
    template_name = 'dashboard-one.html'


class AnalyticsView(TemplateView):
    template_name = 'dashboard-two.html'


class SalesView(TemplateView):
    template_name = 'dashboard-one.html'

class UsersView(TemplateView):
    template_name = 'users.html'

class LoginView(TemplateView):
    template_name = 'login.html'
