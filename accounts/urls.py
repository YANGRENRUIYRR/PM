"""Defines URL patterns for accounts."""

from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views


app_name = 'accounts'
urlpatterns = [
    # Include default auth urls.
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html',redirect_field_name='next'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # Registration page.
    path('register/', views.register, name='register'),
]