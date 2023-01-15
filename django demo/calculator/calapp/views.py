from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def add(request, num1, num2):
    r = (num1 + num2)
    r = str(r)
    return HttpResponse("Sum= " + r)


def diff(request, num1, num2):
    r = (num1 - num2)
    r = str(r)
    return HttpResponse("Difference= " + r)


def pro(request, num1, num2):
    r = (num1 * num2)
    r = str(r)
    return HttpResponse("Product= " + r)


def quo(request, num1, num2):
    r = (num1 / num2)
    r = str(r)
    return HttpResponse("Quotient= " + r)


def calculate(request, num1):
    s = (num1 * num1)
    s = str(s)
    c = (num1 * num1 * num1)
    c = str(c)
    return HttpResponse("Square= " + s + " Cube= " + c)
