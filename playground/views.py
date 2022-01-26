from django.http.request import HttpRequest
from django.shortcuts import render
from store.models import Product, Customer
from django.db.models import Q
from django.http import HttpResponse

# Create your views here.


def say_hello(request):
    # product = Customer.objects.order_by('-first_name')[5:10]
    # products = Customer.objects.filter(first_name__istartswith="c").filter(last_name__istartswith="h")
    # products = Customer.objects.filter(Q(first_name__istartswith="c") | Q(last_name__istartswith="h"))
    products = Customer.objects.values('id','first_name', 'last_name', 'phone')[0:5]
    # print(product)
    return render(request, 'hello.html', {'name': 'Haris', 'products': products})
