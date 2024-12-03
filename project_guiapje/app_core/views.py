from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template  import Template, Context
from django.shortcuts import redirect
import logging
# Create your views here.

def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request,'contact.html')

def custom_404_view(request, exception):
    logging.warning('>>>>> APP_CORE - EXPECTION:' + exception)
    return redirect('https://jfbransou.pythonanywhere.com')
