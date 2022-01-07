from django.shortcuts import render, redirect
from .forms import BookForm
from .models import Books


# Create your views here.


def upload(request):
	if request.method == "POST":
		form = BookForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
		return redirect("application:upload")
	form = BookForm()
	books = Books.objects.all()
	return render(request=request, template_name="main/upload.html", context={'form':form, 'books':books})