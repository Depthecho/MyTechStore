from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Product, Category


def signup_page(request):
    print(request.POST)
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in after successful registration
            login(request, user)
            return redirect('store-page')  # Redirect to the store page after signup
    else:
        form = RegistrationForm()

    return render(request, 'mainpage/signup-page.html', {'form': form})


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('store-page')  # Redirect to the desired page after successful login
        else:
            # Authentication failed, display an error message
            error_message = "Invalid username or password. Please try again."
    else:
        error_message = None
    return render(request, 'mainpage/login-page.html', {'error_message': error_message})


def logout_page(request):
    logout(request)
    return redirect('login-page')


def store_page(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    filter_price_min = request.GET.get('price_min')
    filter_price_max = request.GET.get('price_max')
    sort_by = request.GET.get('sort_by')
    category = request.GET.get('category', 'all')
    items_per_page = request.GET.get('itemsPerPage', 12)

    if filter_price_min:
        products = products.filter(price__gte=filter_price_min)
    if filter_price_max:
        products = products.filter(price__lte=filter_price_max)

    if sort_by == 'price_low':
        products = products.order_by('price')
    elif sort_by == 'price_high':
        products = products.order_by('-price')

    if category != 'all':
        products = products.filter(category__name=category)

    context = {'products': products, 'categories': categories}
    return render(request, 'mainpage/store-page.html', context)


def add_to_favorite(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    user = request.user

    # Добавляем продукт в избранное пользователя
    user.favorite_products.add(product)

    return redirect('store-page')


def remove_from_favorite(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    user = request.user

    # Удаляем продукт из избранного пользователя
    user.favorite_products.remove(product)

    return redirect('store-page')


