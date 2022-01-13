from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import BookForm
from .models import Books


# Create your views here.


def upload(request):
	if request.method == "POST":
		form = BookForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
		return redirect("/")
	form = BookForm()
	books = Books.objects.all()
	return render(request=request, template_name="upload.html", context={'form':form, 'books':books})

def books(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.save()
        return redirect('/')
    else:
        form = BookForm()
        
    return render(request, 'books.html', {"form": form})

def search(request):
    
    if 'book' in request.GET and request.GET["Books"]:
        search_book = request.GET.get("Books")
        searched_book = Books.search_by_title(search_book)
        message = f"{search_book}"

        return render(request, 'searchbar.html',{"message":message,"Books": searched_book})

    else:
        message = "You haven't searched for any book"
        return render(request, 'searchbar.html',{"message":message})