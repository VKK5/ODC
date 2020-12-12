from django.shortcuts import render
from .models import Product
# Create your views here.

def medicines(request):

    prods = Product.objects.all()

    return render(request,'medstore/medicines.html',{'prods':prods})


def medicinedetails(request,prodid):
    
    prod = Product.objects.get(pk=prodid)

    #cart_product_form = CartAddProductForm()
    #return render(request,'bazaar/bazindex.html',{'product':prod,'cart_product_form':cart_product_form})
    return render(request,'medstore/medicinedetails.html',{'product':prod})    