from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect

from mainpage.models import Product


@login_required(login_url='login-page')
def add_to_favorite(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    user = request.user

    # Adding the product to the user's favorites
    user.favorite_products.add(product)

    return redirect('store-page')


@login_required(login_url='login-page')
def remove_from_favorite_store(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    user = request.user

    # Removing the product from the user's favorites
    user.favorite_products.remove(product)

    return redirect('store-page')


def remove_from_favorite(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    user = request.user

    # Removing the product from the user's favorites
    user.favorite_products.remove(product)

    return redirect('favorite-list')


@login_required(login_url='login-page')
def favorite_list(request):
    favorite_products = request.user.favorite_products.all()
    items_per_page = 9
    paginator = Paginator(favorite_products, items_per_page)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'favorite/favorite_list.html', {'favorite_products': page})