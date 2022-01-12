from django.urls.conf import path,include
from django.urls import path, include
from . import views

urlpatterns =[ 
    path('reviews/', views.reviews),
    path("", views.upload, name="upload"),
    path("books/", views.books, name="books"),
    path("upload/", views.upload, name="upload"),
    path('profile', views.profile, name='profile'),
    path('signup/', views.signup,name='signup'),
    path('signup/customer/', views.customer_signup,name='customer_signup'),
    path('signup/author/', views.author_signup,name='author_signup'),
]


