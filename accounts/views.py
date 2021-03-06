from django.shortcuts import render, redirect
from accounts.forms import (
    RegistrationForm,
    UpdationForm
)
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.
# def home(request):
#     data = {'name': ' ', 'age': [1,2,3,4,5]}
#     return render(request, 'accounts/home.html', data)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:home'))
    else:
        form = RegistrationForm
        return render(request, 'accounts/register.html', {'form': form})

def view_profile(request):
    args = {'user': request.user}
    return render(request, 'accounts/profile.html', args)

def edit_profile(request):
    if request.method == 'POST':
        form = UpdationForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return render(request, 'accounts/edit_profile.html', {'form': form})
    else:
        form = UpdationForm(instance=request.user)
        return render(request, 'accounts/edit_profile.html', {'form': form})

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/account/profile')
        else:
            return redirect(reverse('accounts:change_password'))
    else:
        form = PasswordChangeForm(user=request.user)
        return render(request, 'accounts/change_password.html', {'form': form})
