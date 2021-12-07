from django.shortcuts import redirect, render
from .models import DrinksData
from .forms import DrinkForm
from django.contrib.auth.decorators import login_required
import time

# Create your views here.
def base(request):

    return render(request, 'drinks_app/base.html')

def home(request):

    drinksdb = DrinksData.objects.all()

    context = {
        'drinksdb' : drinksdb
    }

    return render(request, 'drinks_app/index.html', context)

def details(request, id):

    drink_details = DrinksData.objects.get(id=id)

    context = {
        'drink_details' : drink_details
    }

    return render(request, 'drinks_app/details.html', context)

@login_required(login_url='login')
def upload(request):

    form = DrinkForm()
    context = {
        'form':form,
    }

    if request.method == 'POST':

        form = DrinkForm(request.POST, request.FILES)

        if form.is_valid():

            form.save()

            time.sleep(2)

            return redirect('home')
    else:
        context

    return render(request, 'drinks_app/upload.html', context)