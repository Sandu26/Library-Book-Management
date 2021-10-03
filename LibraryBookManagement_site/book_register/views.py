from django.shortcuts import render, redirect
from django.db.models.query_utils import Q
from .forms import BookForm
from .models import Book
import os

# send request to view book list
def books_list(request): 
    context = {'books_list': Book.objects.all()}
    return render(request, "book_register/books_list.html", context)

# send request to view book form
def book_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = BookForm()
        else:
            book = Book.objects.get(pk=id)
            form = BookForm(instance=book)
        return render(request, "book_register/book_form.html", {'form': form})
# insert a book to list and view    
    else:
        if id == 0:
            form = BookForm(request.POST)
        else:
            book = Book.objects.get(pk=id)
            form = BookForm(request.POST,instance= book)
        if form.is_valid():
            form.save()
        return redirect('/books')

# delete a book to list and updated view 
def book_delete(request,id):
    book = Book.objects.get(pk=id)
    book.delete()
    return redirect('/books')

# search a book
def search_books(request):
    if request.method == "POST":
        searched = request.POST['searched']
        books = Book.objects.filter(Q(name__contains=searched) | Q(genre__contains=searched))
        return render(request, "book_register/search.html",{'searched': searched, 'books': books})
    else:
        return render(request, "book_register/search.html",{})
# request homepage
def homepage(request):
    return render(request, "book_register/home.html", {})