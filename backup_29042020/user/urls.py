from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views


app_name = "user"

urlpatterns = [
    path('login/',views.userLogin,name="userLogin"),
    path('logout/',views.userLogout,name="userLogout"),
    path('register/',views.userRegister, name="userRegister"),
    path('',include("django.contrib.auth.urls")),
]