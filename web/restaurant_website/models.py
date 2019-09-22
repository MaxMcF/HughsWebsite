from django.contrib.auth.models import User
from django.dispatch import receiver
from django.utils import timezone
from django.db import models
import uuid
# Create your models here.


class Product(models.Model):
	product_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	product_name = models.CharField(max_length=180, default='Untitled')
	price = models.FloatField(blank=True, null=True)
	product_description = models.CharField(max_length=180, default='Untitled')
	date_uploaded = models.DateField(auto_now_add=True)
	date_modified = models.DateField(auto_now=True)

	def __repr__(self):
		return '<Product: {}>'.format(self.product_name)

	def __str__(self):
		return '{}'.format(self.product_name)

class Transaction(models.Model):

	transaction_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transaction')
	transaction_amount = models.FloatField(blank=True, null=True)
	date_updated = models.DateField(auto_now=True)
	date_created = models.DateField(auto_now_add=True)

	def __repr__(self):
		return '<Transaction: {}>'.format(self.name)

	def __str__(self):
		return '{}'.format(self.name)

class Cart(models.Model):
	transaction_id = models.ForeignKey(Transaction, on_delete=models.CASCADE, related_name='cart')
	product_id = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='transaction')

	def __repr__(self):
		return '<Cart Item For Transaction: {}>'.format(self.transaction_id)
		
	def __str__(self):
		return '{}'.format(self.transaction_id)