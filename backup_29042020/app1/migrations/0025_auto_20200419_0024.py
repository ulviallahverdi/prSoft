# Generated by Django 3.0.3 on 2020-04-18 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0024_product_role'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'default_permissions': ('change', 'add', 'delete', 'view')},
        ),
    ]