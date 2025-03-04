from django.http.response import JsonResponse

from django.shortcuts import redirect, render

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from home.models import Order , OrderItem

def index(request):
    orders = Order.objects.filter(user=request.user)
    context = {'orders':orders}
    return render(request,"orders/order.html",context)

def vieworder(request,t_no):
    order = Order.objects.filter(tracking_no=t_no).filter(user=request.user).first()
    orderitem = OrderItem.objects.filter(order=order)
    context = {'order':order ,'orderitem':orderitem}
    return render(request, "orders/orderview.html",context)
    