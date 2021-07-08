from django.shortcuts import render

# Create your views here.
def checkout(request):
    return render(request,'order/checkout.htm')

def quantity(request):
    return render(request,'order/quantity.htm')