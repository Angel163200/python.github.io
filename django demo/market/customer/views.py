from django.shortcuts import render


# Create your views here.

def home1(request):
    return render(request, 'customer/customer.html')
def update_customer(request):
    return render(request, 'common/update_profile.html')