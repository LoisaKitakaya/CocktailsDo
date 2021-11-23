from django.shortcuts import redirect, render

# Create your views here.
def base(request):

    return render(request, 'drinks_app/base.html')

def home(request):

    return render(request, 'drinks_app/index.html')