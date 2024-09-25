from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template  import Template, Context
# Create your views here.

def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request,'contact.html')