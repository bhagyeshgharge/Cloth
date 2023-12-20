from django.shortcuts import render,redirect,HttpResponse
from app.models import Cloth
# Create your views here.

def home(request):
     obj="""{'cloth':[{'id':1,'product':'shirt','size':'xl','price':500}]}
     return render(request,'home.html',obj)"""

     data=Cloth.objects.all()
     obj={'cloth':data}
     return render(request,'home.html',obj)

def addnew(request):
    if request.method=='GET':
         return render(request,'addnew.html')
    else:
         name1=request.POST['name']
         size1=request.POST['size']
         price1=request.POST['price']
         obj=Cloth.objects.create(product=name1,size=size1,price=price1)
         obj.save
         return redirect('/')
    

def edit(request,tid):
     if request.method=='GET':
        obj=Cloth.objects.filter(id=tid)
        return render(request,'edit.html',{'cloth':obj})
     else:
         name1=request.POST['name']
         size1=request.POST['size']
         price1=request.POST['price']
         obj=Cloth.objects.filter(id=tid)         
         obj.update(product=name1,size=size1,price=price1)
         return redirect('/')


def delete(request,tid):
    obj=Cloth.objects.filter(id=tid)
    obj.delete()
    return redirect('/')