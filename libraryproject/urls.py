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
from django.contrib import admin
from django.urls import include, path
import apps.bookmodule.views
from apps.bookmodule import views



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
    path('', views.index, name="bookmodule.index"),  #----------------
    path('list_books/', views.list_books, name="bookmodule.list_books"),
    path('aboutus/', views.aboutus, name="bookmodule.aboutus"),
    path('<int:bookId>/', views.viewbook, name="bookmodule.view_one_book"),
    path('books/', include('apps.bookmodule.urls')),  # Ensure this matches the app's path

]

