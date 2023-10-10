from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404,render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegistrationForm
from .models import Product, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from user_profile.models import UserProfile


def signup_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in after successful registration
            UserProfile.objects.create(user=user)
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


@login_required(login_url='login-page')
def logout_page(request):
    logout(request)
    return redirect('login-page')


def store_page(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    user = request.user

    profile = None
    if request.user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=request.user)
        except UserProfile.DoesNotExist:
            pass

    search_query = request.GET.get('search')
    if search_query:
        products = products.filter(name__icontains=search_query)

    filter_price_min = request.GET.get('price_min')
    filter_price_max = request.GET.get('price_max')
    sort_by = request.GET.get('sort_by')
    category = request.GET.get('category', 'all')

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

    # Processing of the form for selecting the number of products on the page
    if request.method == 'GET' and 'itemsPerPage' in request.GET:
        items_per_page = int(request.GET['itemsPerPage'])
        request.session['items_per_page'] = items_per_page
    else:
        # If the value is not specified in the form, use the stored value in the session
        items_per_page = request.session.get('items_per_page', 12)

    paginator = Paginator(products, items_per_page)
    page = request.GET.get('page')

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {'products': products, 'categories': categories, 'profile': profile}
    return render(request, 'mainpage/store-page.html', context)


def product_detail(request, product_id):
    user = request.user
    try:
        profile = UserProfile.objects.get(user=user)
    except UserProfile.DoesNotExist:
        profile = None
    product = get_object_or_404(Product, id=product_id)
    context = {'product': product, 'profile': profile}
    return render(request, 'mainpage/product_detail.html', context)
