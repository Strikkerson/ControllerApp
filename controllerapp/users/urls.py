from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.register),
    path('login/', views.login),
    path('logout/', views.logout),
]