from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer, Product,Tag,Order

def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_customers = customers.count()
    total_orders = orders.count()
    delivered = Order.objects.filter(status='Delivered').count()
    pending = Order.objects.filter(status='Pending').count()
    context = {'orders':orders,'customers':customers,'total_orders':total_orders,'delivered':delivered,'pending':pending}
    return render(request,"accounts/dashboard.html",context)

def products(request):
    products = Product.objects.all()
    return render(request,"accounts/products.html",{"products":products})

def customer(request):
    return render(request,"accounts/customer.html")