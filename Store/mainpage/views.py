from django.shortcuts import render
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import RegistrationForm


def signup_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in after successful registration
            login(request, user)
            return redirect('store-page')  # Redirect to the store page after signup
    else:
        form = RegistrationForm()

    return render(request, 'mainpage/signup-page.html', {'form': form})


def login_page(request):
    return render(request, 'mainpage/login-page.html')


def store_page(request):
    return render(request, 'mainpage/store-page.html')