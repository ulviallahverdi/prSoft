from django import forms
from django.forms import ModelForm
from app1.models import Product, Test
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class ProductForm(forms.ModelForm):
    location = forms.CharField(max_length=80,required=True,label = "Əşyanın itirildiyi/tapıldığı yer")
    bonus_ammount = forms.IntegerField(max_value=10000, min_value=1,label="Mükafat məbləği")
    class Meta:
        model = Product
        fields = ['fullname','email_address','mobile_number','lostorfound','title','category','location','content','bonus_ammount','image']


class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ['name','number','lostorfound']