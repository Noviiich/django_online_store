from django.contrib import admin
from .models import Product, Customer, Brand

class ProductAdmin(admin.ModelAdmin):
    list_display = ('popularity_score', 'name', 'created_at', 'price', 'in_stock', 'brand', 'image')
    list_filter = ('in_stock',)
    search_fields = ['name', 'description']

# admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(Customer)
admin.site.register(Product, ProductAdmin)


