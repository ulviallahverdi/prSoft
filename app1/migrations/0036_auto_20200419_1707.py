# Generated by Django 3.0.3 on 2020-04-19 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0035_product_fast_service'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='secim',
        ),
        migrations.AlterField(
            model_name='product',
            name='bonus_ammount',
            field=models.IntegerField(max_length=5, verbose_name='Mükafat Məbləği'),
        ),
        migrations.AlterField(
            model_name='product',
            name='content',
            field=models.TextField(max_length=200, null=True, verbose_name='Məzmun'),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Yaradılma tarixi'),
        ),
        migrations.AlterField(
            model_name='product',
            name='email_address',
            field=models.EmailField(max_length=50, null=True, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='product',
            name='fullname',
            field=models.CharField(max_length=50, null=True, verbose_name='Tam adınız'),
        ),
        migrations.AlterField(
            model_name='product',
            name='location',
            field=models.CharField(max_length=80, null=True, verbose_name='Əşyanın itirildiyi/tapıldığı yer'),
        ),
        migrations.AlterField(
            model_name='product',
            name='lostorfound',
            field=models.BooleanField(choices=[(True, 'itirmişəm'), (False, 'tapmışam')], verbose_name='itirmisən?/tapmısan?'),
        ),
        migrations.AlterField(
            model_name='product',
            name='mobile_number',
            field=models.IntegerField(max_length=15, null=True, verbose_name='Mobil Nömrəniz'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Elan adı'),
        ),
    ]
