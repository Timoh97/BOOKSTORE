from . import views
from django.urls import path

urlpatterns =[ 
    path('reviews/', views.reviews),
    path("", views.upload, name="upload"),
    path("books/", views.books, name="books"),
    path("upload/", views.upload, name="upload"),
    
]