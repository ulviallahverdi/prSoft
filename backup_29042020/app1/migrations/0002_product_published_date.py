# Generated by Django 3.0.3 on 2020-04-16 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
