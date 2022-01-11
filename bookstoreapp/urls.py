from django.urls.conf import path
from . import views

urlpatterns=[
    path('profile/<username>/', views.profile, name='profile'),
    path('user_profile/<username>/', views.user_profile, name='user_profile'),
]