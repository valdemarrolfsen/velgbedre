from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Product(models.Model):
	name = models.CharField(max_length=100)
	short_description = models.TextField(blank=True, null=True)
	description = RichTextField()
	image = models.ImageField(upload_to='products/%Y/%m/%d')
	cover_image = models.ImageField(upload_to='packages/%Y/%m/%d', blank=True, null=True)


	class Meta:
		verbose_name = "Product"
		verbose_name_plural = "Products"

	def __str__(self):
		return "{}".format(
			self.name)

class Company(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(blank=True, null=True)
	testemonial = models.TextField(blank=True, null=True)
	logo = models.ImageField(upload_to='logos/%Y/%m/%d')
	product = models.ImageField(upload_to='products/%Y/%m/%d')

	class Meta:
		verbose_name = "Company"
		verbose_name_plural = "Companies"

class Subscriber(models.Model):

	name = models.CharField(max_length=100)
	email = models.CharField(max_length=100)

	class Meta:
		verbose_name = "Subscriber"
		verbose_name_plural = "Subscribers"

class Letter(models.Model):

	name = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	the_lucky_one = models.CharField(max_length=100)

	class Meta:
		verbose_name = "Letter"
		verbose_name_plural = "Letters"

class Package(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField()
	price = models.IntegerField()

	image = models.ImageField(upload_to='packages/%Y/%m/%d', blank=True, null=True)

	def get_products(self):
		return ProductPackage.objects.filter(package = self)

	def __str__(self):
		return "{}".format(self.name)

class ProductPackage(models.Model):
	package = models.ForeignKey(Package, related_name='Pacakge')
	product = models.ForeignKey(Product, related_name='Product')


    
