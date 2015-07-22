from django.contrib import admin
from .models import *

# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
	list_display = ['firstname', 'lastname']

class ProductAdmin(admin.ModelAdmin):
	list_display = ['id', 'name']

class ProductImageAdmin(admin.ModelAdmin):
	list_display = ['name']

class WishAdmin(admin.ModelAdmin):
	list_display = ['priority', 'product', 'user']

class CompanyAdmin(admin.ModelAdmin):
	list_display = ['name', 'code']

class CompanyProductRelationAdmin(admin.ModelAdmin):
	list_display = ['company']

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(Wish, WishAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(CompanyProductRelation, CompanyProductRelationAdmin)