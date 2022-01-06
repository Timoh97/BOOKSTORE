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


