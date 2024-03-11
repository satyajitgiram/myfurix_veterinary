from django.urls import path
from .views import home, contact, shop

urlpatterns = [
    path('', home, name='home'),
    path('shop', shop, name="shop"),
    path('contact', contact, name='contact'),
]
