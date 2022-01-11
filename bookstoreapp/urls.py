from django.urls.conf import path
from . import views

urlpatterns =[ 
    path('reviews/', views.reviews),
    path("", views.upload, name="upload"),
    path("books/", views.books, name="books"),
    path("upload/", views.upload, name="upload"),
    path('profile', views.profile, name='profile'),
]