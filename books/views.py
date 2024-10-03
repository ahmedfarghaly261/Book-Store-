from django.shortcuts import render,redirect
from .models import Book,Users
# Create your views here.
def book(request):
    data=Book.objects.filter(types='trending')
    return render(request,"books/books.html",{'data':data})



def sec_books(request):
    allBooks={"allBooks":Book.objects.filter(types="all books")}
    return render(request,'books/section_books.html',allBooks)


def user(request):
    user=request.POST.get('username')
    password=request.POST.get('password')
    email=request.POST.get('email')
    data=Users(username=user,password=password,email=email)
    if request.method=='POST':
        data.save()
        return redirect(book,)
        
    return render(request,"auths_temp/login.html",)


def book_content(request,book_name):
    book_name=Book.objects.get(name=book_name)
    return render(request,'books/book_content.html',{'book_name':book_name})


def cart(request,bookName):
    bookName=Book.objects.get(name=bookName)
    return render (request,"books/cart.html",{'bookName':bookName})