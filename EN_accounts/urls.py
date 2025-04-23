"""Defines URL patterns for accounts."""

from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
app_name = 'EN_accounts'
urlpatterns = [
    # Include default auth urls.
    path('login/', auth_views.LoginView.as_view(template_name='regiistration/login.html',redirect_field_name='next'), name='login'),
    # Registration page.
    path('register/', views.register, name='register'),
]