from email.policy import default
from enum import unique
from tabnanny import verbose
from django.db import models
from django.core import validators
import re
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, UserManager)
from django.urls import reverse
from django.utils.text import slugify
import os

from django.conf import settings

def user_avatar_path(instance, filename):
        # Extrai a extensão do arquivo original
        ext = filename.split('.')[-1]
        
        # Gera o novo nome do arquivo usando o nome de usuário, com slug para garantir segurança no nome
        filename = f"{slugify(instance.username)}.{ext}"
        
        # Retorna o caminho onde o arquivo será salvo
        return os.path.join('avatars/images', filename)

class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(
        'Nome de Usuário',
        max_length = 30,
        unique=True,
        validators=[validators.RegexValidator(re.compile('^[\w.@+-]+$'),
            'O nome de usuário só pode conter letras, digitos ou os seguintes caracteres: @/.+/-/_',
            'invalid'
        )]
    )
    email = models.EmailField(("Email"), unique=True)
    name = models.CharField('Nome',max_length=100, blank=True)
    is_active = models.BooleanField('Está ativo?', blank=True, default=True)
    is_staff = models.BooleanField('É da equipe?', blank=True, default=False)
    date_joined = models.DateTimeField('Data de Entrada', auto_now_add=True)
    avatar = models.ImageField('Foto de profile',upload_to=user_avatar_path,null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

    def get_short_name(self):
        return self.username
    
    def get_full_name(self):
        return str(self)
    
    def save(self, *args, **kwargs):
        # Verifica se o usuário já tem um avatar
        try:
            old_avatar = User.objects.get(pk=self.pk).avatar
        except User.DoesNotExist:
            old_avatar = None

        # Sobrescreve o arquivo existente
        if old_avatar and old_avatar != self.avatar:
            old_avatar_path = os.path.join(settings.MEDIA_ROOT, old_avatar.name)
            if os.path.isfile(old_avatar_path):
                os.remove(old_avatar_path)

        # Salva o novo avatar, sempre mantendo o mesmo nome de arquivo
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

# um usuário poderá ter "1" ou "N" PasswordResets
class PasswordReset(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name = 'Usuário',
        related_name = 'resets'
    )

    key = models.CharField('Chave', max_length=100, unique=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    confirmed = models.BooleanField('Confirmado?',default=False,blank=True)

    def __str__(self):
        return '{0} em {1}'.format(self.user, self.created_at)
    
    class Meta:
        verbose_name = 'Nova Senha'
        verbose_name_plural = 'Novas Senhas'
        ordering = ['-created_at']
    
