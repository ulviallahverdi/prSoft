# Generated by Django 3.0.5 on 2020-05-02 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0042_auto_20200501_1739'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True, verbose_name='Adiniz')),
                ('number', models.IntegerField(verbose_name='Nomre')),
            ],
        ),
    ]