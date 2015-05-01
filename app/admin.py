from django.contrib import admin
from app.models import *

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
	list_display = ['name']

class CompanyAdmin(admin.ModelAdmin):
	list_display = ['name']

class SubscriberAdmin(admin.ModelAdmin):
	list_display = ['name', 'email']

class LetterAdmin(admin.ModelAdmin):
	list_display = ['the_lucky_one', 'email', 'name']

admin.site.register(Product, ProductAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Subscriber, SubscriberAdmin)
admin.site.register(Letter, LetterAdmin)
