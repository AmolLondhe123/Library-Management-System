from typing_extensions import Self
from django.shortcuts import render,HttpResponse,redirect
from .models import Library,Admin
from django.contrib import messages
# Create your views here.


def index(request):
    return render(request,'home.html')

def view(request):
    books=Library.objects.all()
    context={
        'books':books,
    }
    #print(context)
    return render(request,'home.html',context)

def add(request):
    
    if request.method == 'POST':
        book_name = request.POST['book_name']
        auth_name = request.POST['Auther_name']
        pages = request.POST['pages']
        
        
        new_book=Library(book_title=book_name,book_author=auth_name,book_pages=pages)
        new_book.save()
        messages.success(request,'Book added Successfully')
        return render(request,'add.html')
    elif request.method=='GET':
        return render(request,'add.html')
    else:
        # return HttpResponse("An error Occured! Employee Has Not Been added")
    
        return render(request,'add.html')

def update(request,id=0):
    books=Library.objects.all()
    context={
        'books':books
    }
    if id: 
        book=Library.objects.get(id=id)
        book.delete()
        return render(request,'add.html',context)
    return render(request,'update.html',context)    
def delete(request,id=0):
    books=Library.objects.all()
    context={
        'books':books
    }
    if id: 
     book=Library.objects.get(id=id)
     book.delete()
    return render(request,'delete.html',context)

def sview(request):
    books=Library.objects.all()
    context={
        'books':books,
    }
    #print(context)
    return render(request,'sview.html',context)

def login(request):
     
    if request.method == 'POST':
        email= request.POST['email']
        password = request.POST['pass']
        login=Admin.objects.filter(email=email,password=password).first()
        if login:
            return render(request,'home.html')
            messages.success(request,'Employee added Successfully')
        else:
            return render(request,'login.html')
    return render(request,'login.html')

def signup(request):
    
    if request.method == 'POST':
        name = request.POST['name']
        email= request.POST['email']
        password = request.POST['pass']
        
        
        new=Admin(Uname=name,email=email,password=password)
        new.save()
        # messages.success(request,'Book added Successfully')
    
   
    return render(request,'signup.html')