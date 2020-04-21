from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from user.forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib import messages


def userLogin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request,user)
        else:
            return redirect("/user/login")
        return render(request,"user/login.html")
    return render(request,"user/login.html")

def userLogout(request):
    logout(request)
    return redirect("/")

def userRegister(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form":form
        }
    if form.is_valid():
        f = form.save(commit=False)
        f.set_password(form.cleaned_data["password"])
        f.save()
        user = authenticate(request, username = form.cleaned_data["username"], password = form.cleaned_data["password"])
        login(request, user)
        messages.success(request,"You have successfully registered ...")
        return redirect("/user/login")
    return render(request,"register.html",context)
