from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField
from django_google_maps import fields as map_fields

class Category(models.Model):
    name = models.CharField(max_length=50,null=True,verbose_name="Kateqoriya")

    def __str__(self):
        return self.name

class Product(models.Model):
    bool_choises = ((True, "itirmişəm"),(False, "tapmışam"))
    lostorfound = models.BooleanField(choices=bool_choises,verbose_name="itirmisən?/tapmısan?")
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=50,verbose_name="Elan adı")
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Yaradılma tarixi")
    approve = models.BooleanField(verbose_name="Publish Post",null=False)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    image = models.ImageField(verbose_name="Images")
    location = models.CharField(max_length=80,null=True,verbose_name="Əşyanın itirildiyi/tapıldığı yer")
    content = RichTextField(max_length=200,null=True,verbose_name="Məzmun")
    bonus_ammount = models.IntegerField(verbose_name="Mükafat Məbləği")
    fullname = models.CharField(max_length=50,null=True,verbose_name="Tam adınız")
    mobile_number = models.IntegerField(null=True,verbose_name="Mobil Nömrəniz")
    email_address = models.EmailField(max_length=50,null=True,verbose_name="E-mail")
    fast_service = models.CharField(max_length=20,null=True,verbose_name="Sürətli Xidmət")
    #geolocation = map_fields.GeoLocationField(max_length=100)
    #address = map_fields.AddressField(max_length=200)

    class Meta:
        default_permissions = ("change","add","delete","view")

    def __str__(self):
        return self.title
    

class Website(models.Model):
    title = models.CharField(max_length=100,null=True)
    contact_number = models.IntegerField(null=True)
    support_email = models.EmailField(max_length=40,null=True)
    footer_info = models.CharField(max_length=100)