from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def message(request):
    return HttpResponse("welcome to django")


def message1(request, name):
    return HttpResponse("Hello, Its Django world")


def index(request):
    return render(request, 'index.html', )
