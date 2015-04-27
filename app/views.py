from django.shortcuts import render
from app.models import *

# Create your views here.

def frontpage_view(request):
	products = Product.objects.all()
	companies = Company.objects.all()

	if request.method == "POST":
		sub = Subscriber()
		sub.name = request.POST.get('name')
		sub.email = request.POST.get('email')
		sub.save()
		
	return render(request, 'frontpage.html', {
		'products':products,
		'companies':companies,
		})

def about_view(request):
	return render(request, 'about.html')

def contact_view(request):
	return render(request, 'contact.html')

def order_view(request):
	return render(request, 'order.html')
