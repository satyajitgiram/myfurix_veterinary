from django.db import models
from ckeditor.fields import RichTextField

class Banner(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='hero_banner_images/')

    def __str__(self):
        return self.title
    
class Category(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.ImageField(upload_to='category_icons/')

    def __str__(self):
        return self.title
    
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = RichTextField()
    detailed_description = RichTextField()
    image = models.ImageField(upload_to='product_images/')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    available = models.BooleanField(default=True)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.category.title})"
    


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_gallery/')

    def __str__(self):
        return f"Image for {self.product.title}"
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    date = models.DateField()
    image = models.ImageField(upload_to='blog_images/')
    content = models.TextField()

    def __str__(self):
        return self.title


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE , related_name='product_reviews')
    user_image = models.ImageField(upload_to='review_user_images/')
    name = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    stars = models.PositiveIntegerField(default=1, choices=[(i, str(i)) for i in range(1, 6)])
    content = models.TextField()

    def __str__(self):
        return f"Review by {self.name} - {self.stars} stars"