# Generated by Django 5.0.1 on 2024-09-15 13:50

import project_guiapje.app_accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_accounts', '0002_alter_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=project_guiapje.app_accounts.models.user_avatar_path, verbose_name='Foto de profile'),
        ),
    ]
