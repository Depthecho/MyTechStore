from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from mainpage.forms import RegistrationForm
from mainpage.models import Product, Category


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    user = request.user

    # Добавляем продукт в корзину пользователя
    user.cart_products.add(product)

    return redirect('store-page')


def cart_page(request):
    cart_products = request.user.cart_products.all()  # Получите список товаров, находящихся в корзине пользователя
    return render(request, 'cart/cart-page.html', {'cart_products': cart_products})