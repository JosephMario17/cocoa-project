from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm
from .models import Service, Location
# Create your views here.

def home(request):
    locations = Location.objects.all()
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'base/thank_you.html')

    context = {'locations':locations, 'form': form}
    return render(request, 'base/home.html', context)


def about(request):
    context = {}
    return render(request, 'base/about.html', context)


def services(request):
    products = Service.objects.all()
    
    context = {'products':products}
    return render(request, 'base/services.html', context)

def serviceDetails(request):
    context = {}
    return render(request, 'base/service-details.html', context)


def contact(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'base/thank_you.html')

    context = {'form':form}
    return render(request, 'base/contact.html', context)


def custom(request):
    context = {}
    return render(request, 'base/custom_cocoa.html', context)


def bulk(request):
    context = {}
    return render(request, 'base/bulk_supply.html', context)


def processing(request):
    context = {}
    return render(request, 'base/processing.html', context)


def sourcing(request):
    context = {}
    return render(request, 'base/sourcing.html', context)


def training(request):
    context = {}
    return render(request, 'base/training.html', context)


def thankYou(request):
    context = {}
    return render(request, 'base/thank_you.html', context)


