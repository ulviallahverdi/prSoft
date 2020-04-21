from django.http import HttpResponseRedirect
from django.core.exceptions import PermissionDenied
from django.shortcuts import reverse,redirect
from django.contrib import messages

def add_product_decorator(func):
    def wrap(request,*args, **kwargs):
        if request.user.has_perm("app1.add_product"):
            return func(request, *args, **kwargs)
        else:
            messages.success(request,"You don't have permission to add product")
            return HttpResponseRedirect(reverse("app1:Home"))
    return wrap


def update_product_role(func):
    def wrapper(request, *args, **kwargs):
        if request.user.has_perm("app1.change_product"):
            return func(request, *args, **kwargs)
        else:
            messages.warning(request,"You are not athorized to this page")
            return redirect("app1:viewProducts")
    return wrapper
