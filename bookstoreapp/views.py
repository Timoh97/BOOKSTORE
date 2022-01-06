from django.shortcuts import render

def signup(request):
    '''View function to present users with account choices'''
    title = 'Sign Up'
    return render(request,'registration/signup.html',{'title': title})
