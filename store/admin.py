from django.contrib import admin
from .models import Products, Category
from django.utils.html import format_html

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'category'] #wyswietla w panelu admina

    def image_tag(self, obj): #wyswietla maly obrazek itemu w panelu admina
        return format_html('<img src="{}" width="auto" height="200px" />'.format(obj.image.url))
    image_tag.short_description = 'Product Image Preview'
    readonly_fields = ['image_tag']

admin.site.register(Category)
admin.site.register(Products, ProductAdmin)

