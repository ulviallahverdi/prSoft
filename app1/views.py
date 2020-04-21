from django.shortcuts import render,HttpResponse,redirect, get_object_or_404
from .models import Product
from .forms import ProductForm
from django.contrib.auth.decorators import permission_required, login_required
from app1.decorators import add_product_decorator, update_product_role
from django.contrib import messages
from lazysignup.decorators import allow_lazy_user
from lazysignup import utils
from django.core.paginator import Paginator
from django.contrib.auth.models import Permission, User

def index(request):
    if not request.user.is_authenticated:
        return redirect("user:userLogin")
    else:
        keyword = request.GET.get("keyword")
    if keyword:
        data = Product.objects.filter(approve=1,title=keyword)
        nonapproved = Product.objects.filter(approve=0,title=keyword)
        context = {
        "data":data,
        "nonapproved":nonapproved
        }
        return render(request,"products.html",context)
    data = Product.objects.filter(approve=1)
    nonapproved = Product.objects.filter(approve=0)
    context = {
        "data":data,
        "nonapproved":nonapproved
    }
    return render(request,"products.html",context)

    
    

def products(request):
    keyword = request.GET.get("keyword")
    if keyword:
        data = Product.objects.filter(approve=1,title=keyword)
        nonapproved = Product.objects.filter(approve=0,title=keyword)
        context = {
        "data":data,
        "nonapproved":nonapproved
        }
        return render(request,"products.html",context)
    data = Product.objects.filter(approve=1)
    nonapproved = Product.objects.filter(approve=0)
    context = {
        "data":data,
        "nonapproved":nonapproved
    }
    return render(request,"products.html",context)


@allow_lazy_user
def addProduct(request):
    form = ProductForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        f = form.save(commit=False)
        f.user = request.user
        f.approve = False
        f.save()
        return redirect("app1:viewProducts")
    return render(request,"addproduct.html",{"form":form})


@login_required
def productPublish(request,id):
    Product.objects.filter(id=id).update(approve=True)
    messages.success(request,"Your post has been successfuly published")
    return redirect("app1:viewProducts")


@permission_required("app1.change_product")
#@update_product_role
def updateProduct(request,id):
    product_id = get_object_or_404(Product,id=id)
    form = ProductForm(request.POST or None,instance=product_id)
    if form.is_valid():
        form.save()
        messages.success(request,"Item is successfuly edited...")
        return redirect("app1:viewProducts")
    return render(request,"update.html",{"form":form})

@allow_lazy_user
def AsGuest(request):
    return redirect("app1:viewProducts")    


def listing(request):
    product_list = Product.objects.all()
    paginator = Paginator(product_list,4)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'list.html', {'page_obj': page_obj})