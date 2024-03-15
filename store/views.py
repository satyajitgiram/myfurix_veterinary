from django.shortcuts import render
from .models import Banner, Category
from app.models import Testimonial

def home(request):
    banners = Banner.objects.all()
    categories = Category.objects.all()
    testimonials = Testimonial.objects.all()
    for testimonial in testimonials:
        testimonial.star_range = range(testimonial.star_rating)
    return render(request, 'home.html', {'banners': banners, 'categories': categories, 'testimonials': testimonials})



def contact(request):
    return render(request, 'contact.html')

def shop(request):
    return render(request, 'shop.html')
