from django.shortcuts import render


# Create your views here.

def seat(request):
    return render(request, 'index.html')

def index(request):
    return render(request, 'common/index.html')

def genre(request):
    return render(request, 'common/genre.html')

def about(request):
    return render(request, 'common/about.html')

def single(request):
    return render(request, 'common/single.html')
