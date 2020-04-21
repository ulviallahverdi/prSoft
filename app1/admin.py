from django.contrib import admin
from app1.models import Product, Category

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','created_date','user']
    list_filter = ['created_date']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']