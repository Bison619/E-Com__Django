from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

# Create your views here.
def index(request):
    products = Product.objects.all()
    params= {'product': products}
    return render(request,'shop/index.html',params)

def aboutus(request):
    return render(request,"shop/aboutus.html")

def contactus(request):
    return HttpResponse("this is contactus")

def productview(request):
    return HttpResponse("this is productview")

def tracking(request):
    return HttpResponse("this is tracking")

def checkout(request):
    return HttpResponse("this is checkout")

def search(request):
    return HttpResponse("this is search")