from django.urls import path
from . import views
from apps.bookmodule import views

urlpatterns = [
    path('', views.index, name= "books.index"),
    path('list_books/', views.list_books, name= "books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path('html5/links', views.links, name='book.links'),
    path('html5/text/formatting', views.text_formatting, name='text_formatting'),
    path('html5/listing', views.listing, name='listing'),
    path('html5/tables', views.tables, name='tables'),
    path('search/', views.search_books, name='search_books'),
    path('simple/query/', views.search_books, name='simple_query'),
    path('complex/query', views.search_books, name='complex_query'),

]
