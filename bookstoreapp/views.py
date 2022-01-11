from django.shortcuts import render
from django.http  import HttpResponse
from .models import Profile
from . forms import UpdateUserProfileForm
from django.http  import HttpResponseRedirect

# Create your views here.
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
