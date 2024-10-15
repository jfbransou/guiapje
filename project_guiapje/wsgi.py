"""
WSGI config for project_guiapje project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
import sys

# Adiciona o caminho das bibliotecas do ambiente virtual ao sys.path
sys.path.append('/var/www/guia-pje/venv/lib/python3.12/site-packages')  # Substitua '3.x' pela versão do Python que você está usando

# Adiciona o diretório do seu projeto ao sys.path
sys.path.append('/var/www/guia-pje/project_guiapje')

# Define as configurações do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_guiapje.settings')

# Importa a aplicação WSGI
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
