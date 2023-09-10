from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    # Main
    path('', views.store_page, name='store-page'),

    # Auth
    path('signup/', views.signup_page, name='signup-page'),
    path('login/', views.login_page, name='login-page'),
    path('log-out/', views.logout_page, name='log-out'),
]