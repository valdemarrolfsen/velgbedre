from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
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
			return redirect(reverse('company_frontpage'))
	else:
		userForm = UserProfileForm()

	return render(request, 'intro.html', {
		'company':company,
		'userForm':userForm
	})

def giftcard_view(request):

	title = 'Gavekort'

	logout(request)

	errors = {}

	if request.method == 'POST':
		code = request.POST.get('code')
		giftcode = False
		try:
			giftcode = GiftCardCode.objects.get(code=code)
		except Exception:
			errors['code'] = 'Ugyldig kode'

		if giftcode and not giftcode.used:
			giftcode.used = True
			giftcode.save()
			return redirect(reverse('intro', kwargs={'code':giftcode.company.code}))

	return render(request, 'giftcode.html', {
		'errors': errors
		})

def login_view(request):

	title = 'Logg inn'

	logout(request)

	errors = {}

	if request.method == 'POST':
		loginForm = LoginForm(request.POST)
		if loginForm.is_valid():
			user = loginForm.login(request)

			if user.is_active:
				login(request, user)
				return redirect(reverse('company_frontpage'))
	else:
		loginForm = LoginForm()

	return render(request, 'login.html', {
		'errors': errors,
		'loginForm':loginForm
		})

@login_required
def frontpage_view(request):

	products = request.user.company.get_products()

	numProducts = len(products)

	if request.method == 'POST':
		oldWishes = Wish.objects.filter(user=request.user)

		try:
			product = Product.objects.get(pk=request.POST['productId'])
			selectedType = Type.objects.get(pk=request.POST['typeId'])

			try:
				wish = Wish.objects.get(product=product, user=request.user)
			except:
				wish = Wish()
				wish.user = request.user
				wish.product = product
				wish.productType = selectedType.id
				wish.priority = len(oldWishes) + 1
				wish.save()
				return HttpResponse(content="new", status=200)

			if wish.productType == selectedType.id:
				wish.delete()
				return HttpResponse(content="delete", status=200)
			else:
				wish.productType = selectedType.id
				wish.save()
				return HttpResponse(content="update", status=200)

		except Exception as e:
			return HttpResponse(content="Wishlist failed to update", status=500)
	else:
		#If nothing is posted user gets old wishes if there are any
		wishes = Wish.objects.filter(user=request.user)

		wishlist = []

		for wish in wishes:
			wishlist.append({
				'product' : wish.product.id,
				'type' : wish.productType
			})

	return render(request, 'company_frontpage.html', {
		'products':products,
		'wishlist':wishlist,
		'numProducts': numProducts
	})

@login_required
def wishlist_view(request):
	wishlist = Wish.objects.filter(user=request.user).order_by('priority')
	company = request.user.company

	if request.method == 'POST':
		try:
			wishlist = json.loads(request.POST['wishlist'])

			for i in range(len(wishlist)):
				print(int(wishlist[i]))
				wish = Wish.objects.get(pk=int(wishlist[i]))
				wish.priority = i+1
				wish.save()

		except Exception as e:
			print(e)

	return render(request, 'wishlist.html', {
		'wishlist' : wishlist,
		'company' : company
	})

