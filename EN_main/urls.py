from django.urls import path
from . import views
app_name = 'EN_main'
urlpatterns = [
    path('', views.index, name='index'),
    path('websites/', views.websites, name='websites'),
    path('websites/<int:website_id>/', views.website, name='website'),
    path('new_website/', views.new_website, name='new_website'),
    path('new_username/<int:website_id>/', views.new_username, name='new_username'),
    path('edit_username/<int:username_id>/', views.edit_username, name='edit_username'),
    path('help/', views.help, name='help'),
]