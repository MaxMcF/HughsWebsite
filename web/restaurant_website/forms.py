from django.forms import ModelForm
from .models import Product, Transaction, Cart


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'price', 'product_description']

class TransactionForm(ModelForm):
	class Meta:
		model = Transaction
		fields = ['transaction_id', 'user', 'transaction_amount']
		exclude = ('created_at', 'updated_at',)


class CartForm(ModelForm):
	class Meta:
		model = Cart
		fields = ['transaction_id', 'product_id']
