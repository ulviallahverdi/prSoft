# Generated by Django 3.0.3 on 2020-04-19 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0034_auto_20200419_1659'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='fast_service',
            field=models.CharField(max_length=20, null=True, verbose_name='Sürətli Xidmət'),
        ),
    ]
