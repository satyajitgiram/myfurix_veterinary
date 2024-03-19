from django.urls import path
from .views import home, contact, shop, about, product_detail

urlpatterns = [
    path('', home, name='home'),
    path('products', shop, name="shop"),
    path('contact', contact, name='contact'),
    path('about', about, name='about'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),

]
