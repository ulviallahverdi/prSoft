"""prSoft URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
app_name = "app1"

from django.contrib import admin
from django.urls import path
from app1 import views
from django.conf.urls import url

urlpatterns = [
    path('',views.index, name="viewProducts"),
    path('add/',views.addProduct,name = "addProduct"),
    path('publish/<int:id>',views.productPublish,name="productPublish"),
    path('update/<int:id>',views.updateProduct,name = "updateProduct"),
    path('asGuest',views.AsGuest,name="AsGUest"),
    path('pagi',views.listing,name="listing"),
    path('continueasguest/',views.ContinueAsGuest,name="ContinueAsGuest"),
]