# Generated by Django 3.0.3 on 2020-04-16 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_product_published_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='approve',
            field=models.BooleanField(null=True, verbose_name='Publish Post'),
        ),
    ]