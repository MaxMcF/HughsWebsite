from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Product, Transaction, Cart
from .forms import ProductForm, TransactionForm, CartForm

# Create your views here.


class ProductView(LoginRequiredMixin, ListView):
    template_name = 'orders/product_list.html'
    model = Product
    context_object_name = 'retaurant_website'
    login_url = reverse_lazy('login')

    def get_queryset(self):
        return Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context