# Generated by Django 5.1.6 on 2025-03-06 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_socialmediaaccount_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='address',
            field=models.CharField(blank=True, default=None, null=True, unique=True, verbose_name='Address'),
        ),
    ]
