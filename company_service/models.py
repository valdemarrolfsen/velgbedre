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

class Company(models.Model):
	name = models.CharField(max_length=100)
	greeting = models.TextField()
	email = models.CharField(max_length=100)

	logo = models.ImageField(upload_to='company_logo/%Y/%m/%d')
	background = models.ImageField(upload_to='company_background/%y/%m/%d')

class Product(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()

	who = models.TextField()
	how = models.TextField()
	why = models.TextField()

	background = models.ImageField(upload_to='products/%Y/%m/%d')

	def get_images(self):
		images = ProductImage.objects.filter(product=self)

		img_urls = []

		for image in images:
			img_urls.append(image.image.url)

		return img_urls

class Wish(models.Model):
	product = models.ForeignKey(Product)
	user = models.ForeignKey(UserProfile)

	priority = models.IntegerField()

class ProductImage(models.Model):
	name = models.CharField(max_length=50)
	product = models.ForeignKey(Product)
	image = models.ImageField(upload_to='images/%Y/%m/%d')










