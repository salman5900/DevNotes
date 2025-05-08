from django.shortcuts import render, redirect
from .forms import CustomRegisterForm, CustomLoginForm
from django.contrib.auth import login, logout

def register_view(request):
    if request.method == 'POST':
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            login(request, form.save()) 
            return redirect('homepage')  # Redirect  after successful registration
    else:
        form = CustomRegisterForm()

    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('homepage')
        else:
            print(form.errors)
    else: 
        form = CustomLoginForm()

    return render(request, 'users/login.html', { 'form': form })


def logout_view(request):
    logout(request)
    return redirect('homepage')