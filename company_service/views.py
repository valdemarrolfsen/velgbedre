from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
import json

from .forms import *
from .models import *


# Create your views here.
def intro_view(request, code):

	title = 'Opprett Bruker'

	logout(request)

	company = Company.objects.get(code=code)

	if request.method == 'POST':
		userForm = UserProfileForm(request.POST)
		if userForm.is_valid():
			user = userForm.save(company)
			login(request, user)
			return redirect(reverse('frontpage'))
	else:
		userForm = UserProfileForm()

	return render(request, 'intro.html', {
		'userForm':userForm
	})

@login_required
def frontpage_view(request):

	products = request.user.company.get_products()

	numProducts = len(products)

	if request.method == 'POST':
		oldWishes = Wish.objects.filter(user=request.user)

		#Not to smooth using this in case the system crashes when the new wishes is applied
		oldWishesCopy = []

		for wish in oldWishes:
			oldWishesCopy.append(wish)

		oldWishes.delete()

		try:
			data = json.loads(request.POST['data'])

			wishlist = data['wishlist']
			
			for i in range(len(wishlist)):
				wish = Wish()
				wish.user = request.user

				try:
					wish.product = Product.objects.get(pk=wishlist[i])
				except Exception as e:
					print('My exception occurred, value:', e)

				wish.priority = i + 1
				wish.save()
		except:
			for wish in oldWishesCopy:
				wish.save()

	else:
		#If nothing is posted user gets old wishes if there are any
		wishes = Wish.objects.filter(user=request.user)

		wishlist = []

		for wish in wishes:
			wishlist.append(wish.product.id)

	return render(request, 'company_frontpage.html', {
		'products':products,
		'wishlist':wishlist,
		'numProducts': numProducts
	})

def wishlist_view(request):
	wishlist = Wish.objects.filter(user=request.user)
	return render(request, 'wishlist.html', {
		'wishlist' : wishlist
	})

