
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
from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from .forms import *


def signup(request):
    '''View function to present users with account choices'''
    title = 'Sign Up'
    return render(request,'registration/signup.html',{'title': title})

def customer_signup(request):
    '''View function to sign up as a customer'''
    if request.method == 'POST':
        form = CustomerSignUp(request.POST)
        if form.is_valid():
            user = form.save()
            unhashed_password= form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=unhashed_password)
            login(request, user)
            subject = 'Welcome to the BOOKSTORE!'
            message = f'Hi {user.first_name},\nThe Bookstore would like to officially welcome you to our growing community. Browse the selection of books and find out all your reading tastes, see what you would like to purchase, and place your order.\nRemember to enjoy the app!\n\nKind Regards,\nThe Bookstore Management.'
            email_from = settings.EMAIL_HOST_USER
            recepient_list = [user.email,]
            send_mail(subject,message,email_from,recepient_list)
            messages.success(request, 'Account created successfully! Check your email for a welcome mail.')

            return redirect('/')
    else:
        form= CustomerSignUp()

    title = 'Customer Sign Up'
    return render(request,'registration/signup_form.html',{'title': title,'form':form})

def author_signup(request):
    '''View function to sign up as an author'''
    if request.method == 'POST':
        form = AuthorSignUp(request.POST)
        if form.is_valid():
            user = form.save()
            unhashed_password= form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=unhashed_password)
            login(request, user)
            subject = 'Welcome to the BOOKSTORE!'
            message = f'Hi {user.first_name},\nThe Bookstore would like to officially welcome you to our growing author community. Upload your books and have users browse the selection of books, view your uploaded book, and place their order.\nRemember to enjoy the app!\n\nKind Regards,\nThe Bookstore Management.'
            email_from = settings.EMAIL_HOST_USER
            recepient_list = [user.email,]
            send_mail(subject,message,email_from,recepient_list)
            messages.success(request, 'Account created successfully! Check your email for a welcome mail.')

            return redirect('/')
    else:
        form= AuthorSignUp()

    title = 'Author Sign Up'
    return render(request,'registration/signup_form.html',{'title': title,'form':form})


