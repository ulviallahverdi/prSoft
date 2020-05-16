from django.contrib import admin
from app1.models import Product, Category, Website,Test

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','created_date','user']
    list_filter = ['created_date']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Website)
class WebsiteSettings(admin.ModelAdmin):
    list_display = ['title','contact_number','support_email','footer_info']

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ['name','number']