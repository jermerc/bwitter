from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, ProfileUpdateForm, UserUpdateForm

# Create your views here.



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You are now able to log in.')
            response = redirect('login')
            return response
    else:    
        form = UserRegisterForm()
        
    response = render(request, 'users/register.html', {'form': form})
    return response

# Login required to access profile update page.
@login_required
def profile(request):
    # If request is a valid POST request, generate forms. 
    # If forms are valid, save models to database.
    # Else redirect to profile page with forms filled out but not saved to database.
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Profile Updated')
            response = redirect('profile')
            return response
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)  

    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }

    response = render(request, 'users/profile.html', context)
    return response