from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from user.forms import RegisterForm,QeydiyyatForm
from django.contrib.auth.models import User
from django.contrib import messages
from app1.models import Website


def userLogin(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username = username, password = password)
            if user is not None:
                login(request,user)
                return redirect("/")
            else:
                return redirect("/user/login")
            return render(request,"user/login.html")
        return render(request,"user/login.html")
    else:
        messages.success(request,"You have already logged in")
        return redirect("app1:viewProducts")

def userLogout(request):
    logout(request)
    return redirect("/")

def userRegister(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        confirm = request.POST["confirm"]
        email = request.POST["e-mail"]

        if password != confirm and username:
            messages.warning(request,"Şifrələr uyuşmur, təkrar cəhd edin")
            return redirect("user:userRegister")
        else:
            newUser = User(username=username,email=email)
            newUser.set_password(password)
            getuser = User.objects.filter(username=username).count()
            getuseremail = User.objects.filter(email=email).count()
            if (getuser >= 1 or getuseremail >=1):
                messages.error(request,"Bu istfiadeci adini istifade ede bilmezsiniz")
                return redirect("user:userRegister")
            else:
                newUser.save()
                login(request,newUser,backend='django.contrib.auth.backends.ModelBackend')
                messages.success(request,"You have successfuly registered")
                return redirect("app1:viewProducts")
    else:
        return render(request,"user/register.html")

def UserRegister1(request):
    form = QeydiyyatForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save(commit=False)
        form.user = request.user
        form.save()
        return redirect("app1:viewProducts")
    return render(request,"qeydiyyat.html",{"form":form})

def userProfile(request):
    website_settings = Website.objects.get(id=1)
    return render(request,"user_profile/index.html",{"website_settings":website_settings,})