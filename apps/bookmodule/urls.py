from django.urls import path
from . import views
from apps.bookmodule import views

urlpatterns = [
    path('', views.index, name= "books.index"),
    path('list_books/', views.list_books, name= "books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    #path('filterbooks/', views.filterbooks, name="filterbooks"),

    #path('', views.home, name='home'),

    #path('', views.root_redirect, name='root_redirect'),

]
