from django.contrib.auth import views
from django.contrib import admin
from django.urls import path, re_path, include
from project_guiapje.app_core import views

from django.conf import settings

app_name = 'app_core'

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
]
