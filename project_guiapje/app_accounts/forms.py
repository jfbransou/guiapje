from django import forms
from django.contrib.auth import get_user_model
from project_guiapje.app_core.utils import generate_hash_key
from .models import PasswordReset
from .models import User
from project_guiapje.app_core.mail import send_mail_template

#User = get_user_model()
User = get_user_model()

class PasswordResetForm(forms.Form):

    email = forms.EmailField(label='E-mail')

    def clean_email(self):
         email = self.cleaned_data['email']
         if User.objects.filter(email=email).exists():
             return email
         raise forms.ValidationError('Nenhuma usuário encontrado com este e-mail.')
    
    def save(self):
        user = User.objects.get(email=self.cleaned_data['email'])
        key = generate_hash_key(user.username)
        reset = PasswordReset(key=key, user=user)
        reset.save()
        template_name = 'app_accounts/password_reset_mail.html'
        subject = 'Criar uma nova senha no portal do Guia PJe'
        context = {
            'reset': reset
        }
        send_mail_template(subject,template_name, context, [user.email])

class RegisterForm(forms.ModelForm):

    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmação de senha', widget=forms.PasswordInput)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('A senhas não conferem.')
        return password2

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        
        if commit:
            user.save()
        return user
    
    class Meta:
        model = User
        fields = ['username', 'email', 'name','avatar']
    
class EditAccountForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username','email','name','avatar']


