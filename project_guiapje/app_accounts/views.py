from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import (PasswordChangeForm, SetPasswordForm)
from django.conf import settings

from .forms import RegisterForm, EditAccountForm, PasswordResetForm

from django.contrib.auth import logout as logoutUser, authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from .models import PasswordReset

User = get_user_model()

# Create your views here.

@login_required  # quando isso é feito.. a funcao abaixo chamada esta linha todas vez antes de ser executada
def dashboard(request):
    template_name = 'app_accounts/dashboard.html'
    context = {}
    #context['enrollments'] = Enrollment.objects.filter(user=request.user)
    return render(request, template_name, context)

def register(request):
    template_name = 'app_accounts/register.html'

    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            user = authenticate(username=user.username, password=form.cleaned_data['password1'])
            login(request, user)
            #return redirect(settings.LOGIN_URL)
            return redirect('app_core:home')
        else:
            print ("Formulário é invalido...")
    else:
        print ("Método não é POST...")
        form = RegisterForm()

    context = {
        'form': form,
    }
    return render(request, template_name, context)

def password_reset(request):
    template_name = 'app_accounts/password_reset.html'
    context = {}
    form = PasswordResetForm(request.POST or None)
    print(form)
    if form.is_valid():
        form.save()
        context['success'] = True
    context['form'] = form
    return render(request, template_name, context)

def password_reset_confirm(request, key):
    template_name = 'app_accounts/password_reset_confirm.html'
    context = {}
    reset = get_object_or_404(PasswordReset, key=key)
    form = SetPasswordForm(user=reset.user, data=request.POST or None)
    if form.is_valid():
        form.save()
        context['success'] = True
    context['form'] = form
    return render(request, template_name, context)


@login_required
def logout(request):
    logoutUser(request)
    print ("Sessão finalizada.")
    return redirect(settings.LOGOUT_REDIRECT_URL)

@login_required
def edit(request):
    template_name = 'app_accounts/edit.html'
    context = {}
    if request.method == 'POST':
        form = EditAccountForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            form = EditAccountForm(instance=request.user)
            context['sucess'] = True
    else:
        form = EditAccountForm(instance=request.user)

    context['form'] = form
    return render(request, template_name, context)

@login_required
def edit_password(request):
    template_name = 'app_accounts/edit_password.html'
    context = {}
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            #form = PasswordChangeForm(user=request.user)
            context['sucess'] = True
    else:
        form = PasswordChangeForm(user=request.user)

    context['form'] = form
    return render(request, template_name, context)


