from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404,HttpResponseRedirect, JsonResponse
from django.http import JsonResponse
from .forms import BookForm, UserRegisterForm
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
import json
import datetime
from .models import *
from .utils import cookieCart, cartData, guestOrder
from .forms import UserRegisterForm,ProductForm

# Create your views here.
def index(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	products = Product.objects.all()
	if request.method == 'POST':
			form = ProductForm(request.POST, request.FILES)
			# import pdb; pdb.set_trace()
			if form.is_valid():
					post = form.save(commit=False)
					post.user = request.user
					post.save()
					return HttpResponseRedirect(request.path_info)
	else:
			form = ProductForm()
	params = {
        'products':products,
				'form': form, 
        'cartItems':cartItems
        }
	return render(request, 'order/index.html', params)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            messages.success(request, f'Your account has been created! You are now able to log in {username}.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form}) 

