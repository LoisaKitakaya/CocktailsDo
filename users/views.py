from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout, authenticate as django_authenticate, login as django_login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
import time

# Create your views here.
def signup(request):

    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():

            user = form.save()
            
            print("User created successfully!", user)

            django_login(request, user)

            time.sleep(1)

            return redirect('home')

        else:

            for msg in form.error_messages:
                
                print(form.error_messages[msg])

    else:
        form = UserCreationForm()

    return render(request, 'users/register.html', {'signup_form' : form})

def login(request):

    if request.method == 'POST':

        form = AuthenticationForm(data=request.POST)

        if form.is_valid():

            user = form.get_user()

            django_login(request, user)
            
            print("User logged in successfully!")

            time.sleep(1)

            return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'users/login.html', {'login_form' : form})

def logout(request):

    django_logout(request)
    
    time.sleep(1)

    return redirect('home')