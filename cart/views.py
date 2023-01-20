from django.shortcuts import render, redirect
from .models import Cart, Products, CartItem

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def cart(request):
    #cart = Cart.objects.get(cart_id=_cart_id(request))
    #cart_items = CartItem.objects.filter(cart=cart, is_active=True)
    return render(request, 'cart.html')

def add_cart(request, id):
    cart = Cart.objects.all()
    product = Products.objects.get(id=id)
    cart.add(product)
    return redirect("index")