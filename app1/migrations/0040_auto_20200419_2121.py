# Generated by Django 3.0.3 on 2020-04-19 17:21

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0039_product_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='test',
        ),
        migrations.AlterField(
            model_name='product',
            name='content',
            field=ckeditor.fields.RichTextField(max_length=200, null=True, verbose_name='Məzmun'),
        ),
    ]