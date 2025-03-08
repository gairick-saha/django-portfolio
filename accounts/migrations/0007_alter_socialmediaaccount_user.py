# Generated by Django 5.1.6 on 2025-03-07 09:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_customuser_about_customuser_designation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialmediaaccount',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='social_media_accounts', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]
