from django.contrib import admin
from .models import *

# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
	list_display = ['firstname', 'lastname']

class ProductAdmin(admin.ModelAdmin):
	list_display = ['name']

class ProductImageAdmin(admin.ModelAdmin):
	list_display = ['name']

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
