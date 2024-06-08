from django.contrib import admin
from django.utils.html import format_html
from .models import Banner, Category, Product, Post, ProductImage, Review
from ckeditor.widgets import CKEditorWidget
from django import forms

class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'description')
    search_fields = ('title', 'subtitle')
    list_filter = ('title',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title',)
    list_filter = ('title',)

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    readonly_fields = ('image_tag',)

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="100" />'.format(obj.image.url))
        return ""
    image_tag.short_description = 'Image Preview'


class ProductAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())
    detailed_description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Product
        fields = '__all__'


class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    list_display = ('title', 'category', 'price','available', 'discount_price', 'created_at', 'updated_at', 'image_tag')
    search_fields = ('title', 'category__title')
    list_filter = ('category', 'created_at', 'updated_at')
    list_editable = ('price', 'discount_price')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at', 'image_tag')
    inlines = [ProductImageInline]

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="100" />'.format(obj.image.url))
        return ""
    image_tag.short_description = 'Main Image Preview'

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date')
    search_fields = ('title', 'author')
    list_filter = ('author', 'date')
    ordering = ('-date',)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'stars', 'content', 'user_image_tag')
    search_fields = ('name', 'content')
    list_filter = ('stars', 'date')
    readonly_fields = ('date', 'user_image_tag')

    def user_image_tag(self, obj):
        if obj.user_image:
            return format_html('<img src="{}" width="50" height="50" />'.format(obj.user_image.url))
        return ""
    user_image_tag.short_description = 'User Image'


admin.site.register(Banner, BannerAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(ProductImage)
admin.site.register(Review, ReviewAdmin)
