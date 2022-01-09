from django import forms
from .models import Books


# Create your forms here.
class BookForm(forms.ModelForm):

    class Meta:
        model = Books
        fields = ('file', 'image','author',"year_published",'title','price')