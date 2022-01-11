from django import forms
from .models import Books
from django.forms import fields
from django.forms.widgets import Textarea
from . models import Profile


# Create your forms here.
class BookForm(forms.ModelForm):

    class Meta:
        model = Books
        fields = ('file', 'image','author',"year_published",'title','price')


# Update user profile form
class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name','profile_pic', 'bio']
        
        widgets = {
            'bio': Textarea(attrs={'cols': 20, 'rows': 5}),
        }
