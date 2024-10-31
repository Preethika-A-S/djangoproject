from django.shortcuts import render
from shop.models import Category,Product

from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages


# Create your views here.
def allcategories(request):
    c=Category.objects.all()
    context={'cat':c}
    return render(request,'category.html',context)

def allproducts(request,p):                 #Here p receives the category id
    c=Category.objects.get(id=p)            #Reads a particular category objects using id
    p=Product.objects.filter(category=c)    #Reads all products under a particular category object
    context={'cat':c,'product':p}
    return render(request,'product.html',context)

def alldetails(request,d):
    p=Product.objects.get(id=d)
    context={'product':p}
    return render(request,'detail.html',context)


def register(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        cp=request.POST['cp']
        f=request.POST['f']
        l=request.POST['l']
        e=request.POST['e']

        if(p==cp):
            u=User.objects.create_user(username=u,password=p,first_name=f,last_name=l,email=e)
            u.save()

        else:
            messages.error(request,"Passwords are not same")
        return redirect('shop:categories')


    return render(request,'register.html')

def user_login(request):
    if(request.method=="POST"):
        u = request.POST['u']
        p = request.POST['p']
        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
            return redirect('shop:categories')
        else:
            messages.error(request,"Invalid Credentials")

    return render(request,'login.html')


def user_logout(request):
    logout(request)
    return redirect('shop:categories')

def addcategory(request):
    if(request.method=="POST"):
        n=request.POST.get('n')
        i=request.FILES.get('i')
        d=request.POST.get('d')

        c=Category.objects.create(name=n,image=i,desc=d)
        c.save()

        return redirect('shop:categories')

    return render(request,'addcategory.html')


def addproduct(request):
    if(request.method=="POST"):
        n=request.POST['n']
        d=request.POST['d']
        p=request.POST['p']
        s=request.POST['s']
        c=request.POST['c']
        i=request.FILES.get('i')

        cat=Category.objects.get(name=c)

        p=Product.objects.create(name=n,desc=d,price=p,stock=s,category=cat,image=i)
        p.save()
        return redirect('shop:categories')

    return render(request,'addproduct.html')

def addstock(request,i):
    product=Product.objects.get(id=i)
    if(request.method=="POST"):
        product.stock=request.POST['s']
        product.save()
        return redirect('shop:categories')

    context={'pro': product}
    return render(request,'addstock.html',context)