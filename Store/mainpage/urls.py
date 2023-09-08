from django.urls import path, include
from . import views


urlpatterns = [
    # Main
    path('', views.store_page, name='store-page'),

    # Auth
    path('signup/', views.signup_page, name='signup-page'),
    path('login/', views.login_page, name='login-page'),
]