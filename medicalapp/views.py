from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'medicalapp/index.htm')

def doctor(request):
    return render(request, 'medicalapp/doctor.htm')

def shop(request):
    return render(request, 'medicalapp/shop.htm')

def login(request):
    return render(request, 'medicalapp/login.htm')

def signin(request):
    return render(request, 'medicalapp/signin.htm')