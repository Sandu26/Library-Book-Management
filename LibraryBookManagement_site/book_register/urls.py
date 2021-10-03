from django.urls import path,include
from . import views

urlpatterns = [
    path('books', views.books_list,name='books_list'), # view book list from database
    path('books/<int:id>/', views.book_form,name='book_update'), # update database
    path('books/delete/<int:id>/',views.book_delete,name='book_delete'), # delete book from database
    path('books/new/',views.book_form,name='book_insert'), # insert a book to database and view
    path('books/search_books/',views.search_books,name='search_books'), # searching a book in book list
    path('',views.homepage,name='homepage') 
]