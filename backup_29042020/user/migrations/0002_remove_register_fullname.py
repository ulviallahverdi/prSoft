# Generated by Django 3.0.3 on 2020-04-16 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='fullname',
        ),
    ]
