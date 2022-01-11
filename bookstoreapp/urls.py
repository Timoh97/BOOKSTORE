from django.urls.conf import path
from . import views

urlpatterns=[
    path('profile', views.profile, name='profile'),
    path('', views.reviews)
]