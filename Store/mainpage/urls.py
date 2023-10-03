from django.urls import path, include
from . import views


urlpatterns = [
    # Main
    path('', views.store_page, name='store-page'),
    path('product/<int:product_id>/', views.product_detail, name='product-detail'),


    # Auth
    path('signup/', views.signup_page, name='signup-page'),
    path('login/', views.login_page, name='login-page'),
    path('log-out/', views.logout_page, name='log-out'),
]

