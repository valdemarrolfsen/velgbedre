from django.db import models

# Create your models here.
class Product(models.Model):

	name = models.CharField(max_length=100)
	short_description = models.TextField(blank=True, null=True)
	description = models.TextField(blank=True, null=True)
	image = models.CharField(max_length=40)
	score = models.IntegerField()

	class Meta:
		verbose_name = "Product"
		verbose_name_plural = "Products"

	def __str__(self):
		return "{}-{}".format(
			self.name, self.score)

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

    
