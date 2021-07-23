import service
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db import transaction

from django.shortcuts import redirect, render
from .forms import MicrobiologyForm, ChemistryForm, HematologyForm, BloodBankForm, MolecularDiagnoticsForm, ReproductiveBiologyForm
from lab.models import Lab
from .models import Service

@login_required
@transaction.atomic
def createMicrobiology(request):
    form = MicrobiologyForm(request.POST or None)

    if form.is_valid():
        try : 
            service = form.save(commit=False)
            service.lab = Lab.objects.filter(user=request.user).first()
            service.service_type = request.POST.get('service_type')
            service.save()
            return redirect('/service/list/')
        except e:
            print(e)
            return redirect('/service/list/')
    return render(request,'service/microbiology.htm', {'form' : form})

@login_required
@transaction.atomic
def createChemistry(request):
    form = ChemistryForm(request.POST or None)

    if form.is_valid():
        try : 
            service = form.save(commit=False)
            service.lab = Lab.objects.filter(user=request.user).first()
            service.service_type = request.POST.get('service_type')
            service.save()

        except:
            return redirect('/service/list/')

    return render(request,'service/chemistry.htm', {'form' : form})

@login_required
@transaction.atomic
def createHematology(request):
    form     = HematologyForm(request.POST or None)
    if form.is_valid():
        try : 
            service = form.save(commit=False)
            service.lab = Lab.objects.filter(user=request.user).first()
            service.service_type = request.POST.get('service_type')
            service.save()

        except:
            return redirect('/service/list/')

    return render(request,'service/hematology.htm', {'form' : form})

@login_required
@transaction.atomic
def createBloodBank(request):
    form = BloodBankForm(request.POST or None)
    if form.is_valid():
        try : 
            service = form.save(commit=False)
            service.lab = Lab.objects.filter(user=request.user).first()
            service.service_type = request.POST.get('service_type')
            service.save()

        except:
            return redirect('/service/list/')

    return render(request,'service/bank.htm', {'form' : form})

@login_required
@transaction.atomic
def createMolecularDiagnotics(request):
    form = MolecularDiagnoticsForm(request.POST or None)
    if form.is_valid():
        try : 
            service = form.save(commit=False)
            service.lab = Lab.objects.filter(user=request.user).first()
            service.service_type = request.POST.get('service_type')
            service.save()

        except:
            return redirect('/service/list/')

    return render(request,'service/diagnotics.htm', {'form' : form}) 

@login_required
@transaction.atomic
def createReproductiveBiology(request):
    form = ReproductiveBiologyForm(request.POST or None)
    if form.is_valid():
        try : 
            service = form.save(commit=False)
            service.lab = Lab.objects.filter(user=request.user).first()
            service.service_type = request.POST.get('service_type')
            service.save()

        except:
            return redirect('/service/list/')

    return render(request,'service/reproductive.htm', {'form' : form})           

@login_required
def listServices(request):
    try :
        context={
                'topic':'Dashboard',
                'account': 'Home',
                'recent_page': 'My Product',
                }

        return render(request,'service/list.htm',{'context': context})
    except:
        return redirect('/lab/dashboard/')

@login_required
def detailService(request,id):
    try:
        context={
                'topic':'Dashboard',
                'account': 'Home',
                'recent_page': 'My Product',
                }

        return render(request,'service/detail.htm', {'context' : context})
    except:

        return redirect('/lab/dashboard/')

@login_required
def bookService(request):
    try :
        context={
                'topic':'Dashboard',
                'account': 'Home',
                'recent_page': 'Shop',
                }

        return render(request,'service/shop.htm',{'context': context})
    except:
        return redirect('/customer/dashboard/')

@login_required
def bookServiceDetail(request,id):
    try:
        context={
                'topic':'Dashboard',
                'account': 'Home',
                'recent_page': 'Product Detail',
                }

        service = Service.objects.get(id=id)

        return render(request,'lab/customer_detail.htm', {'context' : context,'service': service})
    except:
        return redirect('/lab/dashboard/')
    