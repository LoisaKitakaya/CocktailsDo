from django.shortcuts import redirect, render
from .models import DrinksData
from .forms import DrinkForm
from django.http import HttpResponse
import time

# Create your views here.
def base(request):

    return render(request, 'drinks_app/base.html')

def error_404(request, exception):

    return render(request, 'drinks_app/404.html', status=404)

def home(request):

    drinksdb = DrinksData.objects.all()

    print('Output: ', drinksdb)

    context = {
        'drinksdb' : drinksdb
    }

    return render(request, 'drinks_app/index.html', context)

def details(request, id):

    drink_details = DrinksData.objects.get(id=id)

    print('Output: ', drink_details)

    context = {
        'drink_details' : drink_details
    }

    return render(request, 'drinks_app/details.html', context)

def upload(request):

    form = DrinkForm()
    context = {
        'form':form,
    }

    if request.method == 'POST':

        form = DrinkForm(request.POST, request.FILES)

        if form.is_valid():

            form.save()
            
            print("Uploaded successfully!")

            time.sleep(2)

            return redirect('home')
    else:
        context

    return render(request, 'drinks_app/upload.html', context)