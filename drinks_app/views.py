from django.shortcuts import redirect, render
from .models import DrinksData

# Create your views here.
def base(request):

    return render(request, 'drinks_app/base.html')

def error_404(request, exception):

    return render(request, 'drinks_app/404.html', status=404)

def home(request):

    drinksdb = DrinksData.objects.all()

    print('myoutput', drinksdb)

    context = {
        'drinksdb' : drinksdb
    }

    return render(request, 'drinks_app/index.html', context)