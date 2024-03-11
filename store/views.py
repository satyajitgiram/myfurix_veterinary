from django.shortcuts import render
from .models import Banner, Category

def home(request):
    banners = Banner.objects.all()
    categories = Category.objects.all()
    return render(request, 'home.html', {'banners': banners, 'categories': categories})


def contact(request):
    return render(request, 'contact.html')

def shop(request):
    return render(request, 'shop.html')
