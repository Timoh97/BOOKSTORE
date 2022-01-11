
from django.shortcuts import render
from django.http  import HttpResponse
from .models import Profile
from . forms import UpdateUserProfileForm
from django.http  import HttpResponseRedirect

# Create your views here.
from django.shortcuts import render, redirect
from .forms import BookForm
from .models import Books

# Create your views here.
def reviews(request):
    return render(request, 'index.html')




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
def profile(request):
    current_user=request.user
           
    if request.method == 'POST':
        # user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
    #     if user_form.is_valid() and profile_form.is_valid():
    #         user_form.save()
    #         profile_form.save()
    #         return HttpResponseRedirect(request.path_info)
    # else:
    #     user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateUserProfileForm(instance=request.user.profile)

    return render(request, 'books/profile.html')
def reviews(request):
    return render(request, 'index.html')
