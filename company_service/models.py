from django.db import models
from django.contrib.auth.models import (
	BaseUserManager, AbstractBaseUser
)
from velgbedre import settings


class MyUserManager(BaseUserManager):
	def create_user(self, firstname, lastname, email, address, post_nr, post_place, password=None):

		if not email:
			raise ValueError('Users must have an email address')

		user = self.model(
			email=MyUserManager.normalize_email(email),
			firstname=firstname,
			lastname=lastname,
			address=address,
			post_nr=post_nr,
			post_place=post_place
		)

		user.is_active = True
		user.set_password(password)
		user.save(using=self._db)

		return user

	def create_superuser(self, firstname, lastname, email, address, post_nr, post_place, password=None):

		u = self.create_user(email=email,
						password=password,
						firstname=firstname,
						lastname = lastname,
						address=address,
						post_nr=post_nr,
						post_place=post_place
					)
		u.is_admin = True
		u.is_active = True
		u.save(using=self._db)
		return u

class Company(models.Model):
	code = models.CharField(max_length=50)
	name = models.CharField(max_length=100)
	greeting = models.TextField()
	email = models.CharField(max_length=100)

	logo = models.ImageField(upload_to='company_logo/%Y/%m/%d')
	background = models.ImageField(upload_to='company_background/%y/%m/%d')

	def get_products(self):
		relations = CompanyProductRelation.objects.filter(company=self)
		products = []

		for relation in relations:
			products.append(relation.product)

		return products




class UserProfile(AbstractBaseUser):
	email = models.EmailField(
						verbose_name='email address',
						max_length=255,
						unique=True,
					)
	firstname = models.CharField(max_length=50)
	lastname = models.CharField(max_length=50)
	address = models.CharField(max_length=50)
	post_nr = models.IntegerField()
	post_place = models.CharField(max_length=50)
	is_active = models.BooleanField(default=False)
	is_admin = models.BooleanField(default=False)

	company = models.ForeignKey(Company, null=True, blank=True)

	objects = MyUserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['firstname', 'lastname', 'address', 'post_nr', 'post_place']

	def get_full_name(self):
		# The user is identified by their email address
		return self.firstname + ' ' + self.lastname

	def get_short_name(self):
		# The user is identified by their email address
		return self.email

	def has_perm(self, perm, obj=None):
		"Does the user have a specific permission?"
		# Simplest possible answer: Yes, always
		return True

	def has_module_perms(self, app_label):
		"Does the user have permissions to view the app `app_label`?"
		# Simplest possible answer: Yes, always
		return True

	def __unicode__(self):
		return self.email

	@property
	def is_staff(self):
		"Is the user a member of staff?"
		# For now: All admins are staff
		return self.is_admin

class Product(models.Model):
	name = models.CharField(max_length=100)
	small_description = models.TextField()
	description = models.TextField()

	employment = models.TextField()
	location = models.TextField()
	cooperation = models.TextField()
	wages = models.TextField()
	economic_distribution = models.TextField()
	ownership = models.TextField()
	material_selection = models.TextField()
	environmental_impact = models.TextField()
	certification = models.TextField()

	background = models.ImageField(upload_to='products/%Y/%m/%d')

	def get_images(self):
		images = ProductImage.objects.filter(product=self)

		img_urls = []

		for image in images:
			img_urls.append(image.image.url)

		return img_urls

	def get_types(self):
		return Type.objects.filter(product=self)



class CompanyProductRelation(models.Model):
	company = models.ForeignKey(Company)
	product = models.ForeignKey(Product)


class Wish(models.Model):
	product = models.ForeignKey(Product)
	user = models.ForeignKey(UserProfile)
	productType = models.IntegerField(null=True, blank=True)

	priority = models.IntegerField()

class ProductImage(models.Model):
	name = models.CharField(max_length=50)
	product = models.ForeignKey(Product)
	image = models.ImageField(upload_to='images/%Y/%m/%d')

class Type(models.Model):
	name = models.CharField(max_length=50)
	product = models.ForeignKey(Product)












