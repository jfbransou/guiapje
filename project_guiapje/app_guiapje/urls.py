from django.urls import path
from django.urls import re_path
from . import views

app_name = 'app_guiapje'

urlpatterns = [
    path('', views.home, name='home'),
    #path('guiapje_completo/', views.guiapje_completo, name='guiapje_completo'),
    #path('guiapje_completo/<int:page_number>/', views.guiapje_completo, name='guiapje_completo'),
    re_path(r'^guiapje_completo(?:/(?P<page_number>\d+))?/$', views.guiapje_completo, name='guiapje_completo'),
]