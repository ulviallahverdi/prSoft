from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User

class UserExt(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(verbose_name="Profile Image")