# Generated by Django 3.0.3 on 2020-04-16 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(blank=True, max_length=100, null=True)),
                ('username', models.CharField(blank=True, max_length=25, null=True)),
                ('password', models.CharField(max_length=50, null=True)),
                ('confirm_password', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
