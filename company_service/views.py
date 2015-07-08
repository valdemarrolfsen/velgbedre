from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from .forms import *

# Create your views here.
def intro_view(request):

	title = 'Opprett Bruker'

	if request.method == 'POST':
		userForm = UserProfileForm(request.POST)
		if userForm.is_valid():
			userForm.save()
			return redirect(reverse('frontpage'))
	else:
		userForm = UserProfileForm()

	return render(request, 'intro.html', {
		'userForm':userForm
	})

@login_required
def frontpage_view(request):
	products = Product.objects.all()

	return render(request, 'company_frontpage.html', {
		'products':products
		})

def wishlist_view(request):
	return render(request, 'wishlist.html')

