from django.urls import path
from . import views

  


urlpatterns = [
  
    path("", views.upload, name="upload"),
    path("books/", views.books, name="books"),
    path("upload/", views.upload, name="upload"),
    path("searchbar/", views.search, name="search"),
    
]