from django.shortcuts import render
from .models import Kind, Item
# Create your views here.

def index(request):
    
    kinds = Kind.objects.all()
    
    return render(request, 'index.html', context={'kinds' :kinds})

def catalog(request):
    items = Item.objects.all()
    return render(request, 'catalog.html', context={'items':items})    

def catalog_filter(request, kind_id):
    items = Item.objects.filter(items=kind_id)
    return render(request, 'catalog.html', context={'items':items}) 