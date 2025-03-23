from django.shortcuts import render
from django.http import HttpResponse
from apps.bookmodule.models import Book
from .models import Book
from django.db import models


def index(request):
   return render(request, "bookmodule/index.html")

def list_books(request):
   return render(request, 'bookmodule/list_books.html')

def aboutus(request):
   return render(request, 'bookmodule/aboutus.html')

def viewbook(request, bookId):
   return render(request, 'bookmodule/one_book.html')

from .models import Book

def search_books(request):
   if request.method == "POST":
      keyword = request.POST.get('keyword', '').strip().lower()
      is_title = request.POST.get('option1')
      is_author = request.POST.get('option2')

      books = Book.objects.all()

      if keyword:
            if is_title and is_author:
               books = books.filter(
                  models.Q(title__icontains=keyword) | models.Q(author__icontains=keyword)
               )
            elif is_title:
               books = books.filter(title__icontains=keyword)
            elif is_author:
               books = books.filter(author__icontains=keyword)
            else:
               books = []

      return render(request, 'bookmodule/bookList.html', {'books': books})


   return render(request, 'bookmodule/search.html')
def __getBooksList():
   book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
   book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
   book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
   return [book1, book2, book3]

def links(request):
   return render(request, 'bookmodule/html5/links.html')
def text_formatting(request):
   return render(request, 'bookmodule/html5/text_formatting.html')
def listing(request):
   return render(request, 'bookmodule/html5/listing.html')

def tables(request):
   return render(request, 'bookmodule/html5/tables.html')


def simple_query(request):
   mybooks=Book.objects.filter(title__icontains='and') # <- multiple objects
   return render(request, 'bookmodule/bookList.html', {'books':mybooks})


def complex_query(request):
   mybooks=books=Book.objects.filter(author__isnull = False).filter(title__icontains='and').filter(edition__gte = 2).exclude(price__lte = 100)[:10]
   if len(mybooks)>=1:
      return render(request, 'bookmodule/bookList.html', {'books':mybooks})
   else:
      return render(request, 'bookmodule/index.html')
