# Generated by Django 3.0.3 on 2020-04-19 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0037_auto_20200419_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='bonus_ammount',
            field=models.IntegerField(verbose_name='Mükafat Məbləği'),
        ),
        migrations.AlterField(
            model_name='product',
            name='mobile_number',
            field=models.IntegerField(null=True, verbose_name='Mobil Nömrəniz'),
        ),
    ]
