from django.urls import path, include
from . import views
urlpatterns=[
    path('signup/', views.signup,name='signup'),
    path('signup/customer/', views.customer_signup,name='customer_signup'),
    
]
