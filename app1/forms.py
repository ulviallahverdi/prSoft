from django import forms
from django.forms import ModelForm
from app1.models import Product
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class ProductForm(forms.ModelForm):
    location = forms.CharField(max_length=80,required=True,label = "Əşyanın itirildiyi/tapıldığı yer")
    bonus_ammount = forms.IntegerField(max_value=10000, min_value=1,label="Mükafat məbləği")
    image = forms.ImageField(label="Fotoşəkil")
    fast_service = forms.CharField(max_length=20,label="Sürətli Xidmət")
    class Meta:
        model = Product
        fields = ['fullname','email_address','mobile_number','lostorfound','title','category','image','location','content','bonus_ammount','fast_service']