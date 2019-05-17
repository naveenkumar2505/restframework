from django.contrib import admin
from .models import Product
class ProductAdmin(admin.ModelAdmin):
    list_display = ['pid','pname','pcost','pdesc']
admin.site.register(Product,ProductAdmin)
