from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Order
from mainpage.models import Product
from cart.models import CartItem
from user_profile.models import UserProfile


@login_required(login_url='login-page')
def orders_page(request):
    orders = Order.objects.order_by('-order_date')
    user = request.user
    try:
        profile = UserProfile.objects.get(user=user)
    except UserProfile.DoesNotExist:
        profile = None

    context = {
        'profile': profile,
        'orders': orders,
    }

    return render(request, 'orders/orders_page.html', context)


@login_required(login_url='login-page')
def add_to_order(request):
    user = request.user
    order, created = Order.objects.get_or_create(user=user, total_price=0)

    # Get all the items in the current user's cart
    cart_items = CartItem.objects.filter(user=user)

    for cart_item in cart_items:
        product = cart_item.product
        order.products.add(product)
        order.total_price += product.price

    cart_items.delete()

    order.save()

    return redirect('orders')


@login_required(login_url='login-page')
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    context = {
        'order': order,
    }

    return render(request, 'orders/order_detail.html', context)