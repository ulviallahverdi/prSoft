# Generated by Django 3.0.3 on 2020-04-19 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0030_auto_20200419_1322'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='location',
            field=models.CharField(max_length=80, null=True),
        ),
    ]