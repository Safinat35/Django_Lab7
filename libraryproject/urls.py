"""
URL configuration for libraryproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import include, path
# import apps.bookmodule.views
# from apps.bookmodule import views
from django.contrib import admin
from django.urls import path, include
from apps.bookmodule.views import home, index  # Import necessary views
from django.shortcuts import render  # Import render function


urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('books/', include("apps.bookmodule.urls")),
    # path('users/', include("apps.usermodule.urls")),
    # path('list_books/', views.list_books, name= "books.list_books"),
    # path('', views.index, name='books.index'),
    # path('aboutus/', views.aboutus, name='books.aboutus'), 
    # path('', views.index, name= "books.index"),
    # path('list_books/', views.list_books, name= "books.list_books"),
    # path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
    # path('aboutus/', views.aboutus, name="books.aboutus"),
    # path('', views.index, name="bookmodule.index"),  #----------------
    # path('list_books/', views.list_books, name="bookmodule.list_books"),
    # path('aboutus/', views.aboutus, name="bookmodule.aboutus"),
    # path('<int:bookId>/', views.viewbook, name="bookmodule.view_one_book"),
    # path('books/', include('apps.bookmodule.urls')),  # Ensure this matches the app's path
    
    path('', home, name='home'),  # Set the homepage
    path('books/', include('apps.bookmodule.urls')),  # Include bookmodule URLs
    
    # HTML5-related pages
    path('books/html5/links/', lambda request: render(request, 'bookmodule/html5/links.html')),
    path('books/html5/text/formatting/', lambda request: render(request, 'bookmodule/html5/text_formatting.html')),
    path('books/html5/listing/', lambda request: render(request, 'bookmodule/html5/listing.html')),
    path('books/html5/tables/', lambda request: render(request, 'bookmodule/html5/tables.html')),
    path('books/search/', lambda request: render(request, 'bookmodule/search.html')),

    path('admin/', admin.site.urls),
]

