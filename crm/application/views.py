from django.shortcuts import render
from django.http import HttpResponse

from .models import *

# Create your views here.

def home(request):
    products = Product.objects.all()
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status = 'Pending').count()

    context = {'orders': orders, 'customers': customers,'products':products
               ,'total_orders':total_orders,'delivered':delivered,'pending':pending
               }

    return render(request,'application/dashboard.html', context)

