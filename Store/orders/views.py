from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404, redirect
from .models import Order
from mainpage.models import Product
from cart.models import CartItem
from user_profile.models import UserProfile


# The order page display function
@login_required(login_url='login-page')
def orders_page(request):
    user = request.user

    # Working with the display of the user's avatar
    try:
        profile = UserProfile.objects.get(user=user)
    except UserProfile.DoesNotExist:
        profile = None

    all_orders = Order.objects.all()

    orders_per_page = 15

    paginator = Paginator(all_orders, orders_per_page)
    page = request.GET.get('page')

    try:
        orders = paginator.page(page)
    except PageNotAnInteger:
        orders = paginator.page(1)
    except EmptyPage:
        orders = paginator.page(paginator.num_pages)

    # Receiving user orders
    orders = Order.objects.filter(user=user).order_by('-order_date')

    context = {
        'profile': profile,
        'orders': orders,
    }

    return render(request, 'orders/orders_page.html', context)


# The function of adding products to the order
@login_required(login_url='login-page')
def add_to_order(request):
    user = request.user
    order, created = Order.objects.get_or_create(user=user, total_price=0)

    # Get all the items in the current user's cart
    cart_items = CartItem.objects.filter(user=user)

    # Working with goods inside an order
    for cart_item in cart_items:
        product = cart_item.product
        order.products.add(product)
        order.total_price += product.price

    # Removing items from the shopping cart after purchasing an item
    cart_items.delete()

    order.save()

    return redirect('orders')


# The function of displaying each order separately
@login_required(login_url='login-page')
def order_detail(request, order_id):
    user = request.user

    # Working with the display of the user's avatar
    try:
        profile = UserProfile.objects.get(user=user)
    except UserProfile.DoesNotExist:
        profile = None

    # Getting an order from a request
    order = get_object_or_404(Order, id=order_id, user=user)

    order_items = order.products.all().order_by('id')
    items_per_page = 12

    paginator = Paginator(order_items, items_per_page)
    page = request.GET.get('page')

    try:
        order_items = paginator.page(page)
    except PageNotAnInteger:
        order_items = paginator.page(1)
    except EmptyPage:
        order_items = paginator.page(paginator.num_pages)

    context = {
        'order': order,
        'profile': profile,
        'order_items': order_items,
    }

    return render(request, 'orders/order_detail.html', context)