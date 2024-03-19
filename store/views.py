from django.shortcuts import render
from .models import Banner, Category, Product, Post
from app.models import Testimonial

def home(request):
    banners = Banner.objects.all()
    categories = Category.objects.all()
    testimonials = Testimonial.objects.all()
    products = Product.objects.all()
    latest_posts = Post.objects.order_by('-date')[:3]

    for testimonial in testimonials:
        testimonial.star_range = range(testimonial.star_rating)
    return render(request, 'home.html', {'banners': banners,'latest_posts': latest_posts, 'products': products, 'categories': categories, 'testimonials': testimonials})



def contact(request):
    return render(request, 'contact.html')

def shop(request):
    products = Product.objects.all()
    return render(request, 'shop.html', {'products': products})

def about(request):
    testimonials = Testimonial.objects.all()

    return render(request, 'about.html', {'testimonials': testimonials})



from django.shortcuts import render, get_object_or_404
from .models import Product

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product_detail.html', {'product': product})
