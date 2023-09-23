from django.urls import path, include
from . import views


urlpatterns = [
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.cart_page, name='cart'),
]