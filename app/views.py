from django.shortcuts import render
from app.models import *
from .mail_sender import Mail_sender

# Create your views here.

def frontpage_view(request):
	products = Product.objects.all()
	companies = Company.objects.all()

	if request.method == "POST":
		if 'other_name' in request.POST:
			let = Letter()
			let.name = request.POST.get('name')
			let.email = request.POST.get('email')
			let.the_lucky_one = request.POST.get('other_name')
			let.save()
		elif 'frontpage_email' in request.POST:
			Mail_sender.send_cat_request(request.POST.get('frontpage_email'))
		else:
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
