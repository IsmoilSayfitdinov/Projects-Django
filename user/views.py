from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomAuthenticationForm
   
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Akkount {username} yaratildi!')
            return redirect('pages:home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'login-register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('pages:home')
            else:
                messages.error(request, 'Xato foydalanuvchi nomi yoki parol!')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login-register.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('users:login')

