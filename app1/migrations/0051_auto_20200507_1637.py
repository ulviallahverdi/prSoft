# Generated by Django 3.0.5 on 2020-05-07 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0050_website_footer_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='content',
            field=models.CharField(max_length=200, null=True, verbose_name='Məzmun'),
        ),
    ]
