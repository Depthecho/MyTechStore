from django.db.models import Sum
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from mainpage.forms import RegistrationForm
from mainpage.models import Product, Category
from .models import CartItem


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    user = request.user

    # Trying to find an existing product in the user's cart
    cart_item, created = CartItem.objects.get_or_create(user=user, product=product)

    if not created:
        # If the product was already in the cart, we increase its quantity by 1
        cart_item.quantity += 1
        cart_item.save()

    return redirect('store-page')


def cart_page(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_quantity = cart_items.aggregate(total_quantity=Sum('quantity'))['total_quantity']
    return render(request, 'cart/cart-page.html', {'cart_items': cart_items, 'total_quantity': total_quantity})


def remove_from_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    user = request.user

    # Trying to find an existing product in the user's cart
    try:
        cart_item = CartItem.objects.get(user=user, product=product)
        if cart_item.quantity > 1:
            # If the user has more than one copy of the product, reduce the quantity by 1
            cart_item.quantity -= 1
            cart_item.save()
        else:
            # If the user has only one copy of the product, we remove it from the basket
            cart_item.delete()
    except CartItem.DoesNotExist:
        pass

    return redirect('cart')