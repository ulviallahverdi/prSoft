from django.shortcuts import render,HttpResponse,redirect, get_object_or_404
from .models import Product, Category, Website
from .forms import ProductForm,TestForm
from django.contrib.auth.decorators import permission_required, login_required
from app1.decorators import add_product_decorator, update_product_role
from django.contrib import messages
from lazysignup.decorators import allow_lazy_user
from lazysignup import utils
from django.core.paginator import Paginator
from django.contrib.auth.models import Permission, User

# def index(request):
#     category = request.GET.get("category")
#     if category:
#         data = Product.objects.filter(approve=1,category=category)
#         website_settings = Website.objects.get(id=1)
#         categories = Category.objects.all()
#         nonapproved = Product.objects.filter(approve=0)
#         context = {
#             "data":data,
#             "nonapproved":nonapproved,
#             "categories":categories,
#             'website_settings':website_settings,
#         }
#         return render(request,"index.html",context)

#     if not request.user.is_authenticated:
#         return redirect("user:userLogin")
#     else:
#         keyword = request.GET.get("keyword")
#         if keyword:
#             data = Product.objects.filter(approve=1,title=keyword)
#             categories = Category.objects.all()
#             nonapproved = Product.objects.filter(approve=0,title=keyword)
#             context = {
#             "data":data,
#             "nonapproved":nonapproved,
#             "categories":categories,
#             }
#             return render(request,"index.html",context)
#         data = Product.objects.filter(approve=1)
#         website_settings = Website.objects.get(id=1)
#         categories = Category.objects.all()
#         nonapproved = Product.objects.filter(approve=0)
#         context = {
#             "data":data,
#             "nonapproved":nonapproved,
#             "categories":categories,
#             'website_settings':website_settings,
#         }
#         return render(request,"index.html",context)


def index(request):
    #get all categories
    category = request.GET.get("category")
    #if there is category search then search based on category keyword
    if category:
        data = Product.objects.filter(approve=1,category=category)
        website_settings = Website.objects.get(id=1)
        categories = Category.objects.all()
        nonapproved = Product.objects.filter(approve=0)
        context = {
            "data":data,
            "nonapproved":nonapproved,
            "categories":categories,
            'website_settings':website_settings,
        }
        return render(request,"index.html",context)

    elif not request.user.is_authenticated:
        return redirect("user:userLogin")
    else:
        keyword = request.GET.get("keyword")
        if keyword:
            data = Product.objects.filter(approve=1,title__contains =keyword)
            categories = Category.objects.all()
            nonapproved = Product.objects.filter(approve=0,title=keyword)
            website_settings = Website.objects.get(id=1)
            context = {
            "data":data,
            "nonapproved":nonapproved,
            "categories":categories,
            'website_settings':website_settings,
            }
            return render(request,"index.html",context)
        items = Product.objects.filter(approve=1)
        website_settings = Website.objects.get(id=1)
        categories = Category.objects.all()

        paginator = Paginator(items, 40) #Show 3 items per page
        page_number = request.GET.get('page')
        data = paginator.get_page(page_number)
        # nonapproved = Product.objects.filter(approve=0)
        context = {
        "data":data,
        "categories":categories,
        "website_settings":website_settings,
        }
        return render(request,"index.html",context)


@allow_lazy_user
@login_required
def addProduct(request):
    if request.user:
        form = ProductForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            return redirect('app1:viewProducts')
        website_settings = Website.objects.get(id=1)
        return render(request,"addproduct.html",{"form":form,"website_settings":website_settings})
    else:
        return redirect("user:userLogin")

@allow_lazy_user
def ContinueAsGuest(request):
    return redirect("app1:addProduct")

    

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


def fortest(request):
    form = TestForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("/")
    context = {
        "form":form,
    }
    return render(request,"fortest.html",context)