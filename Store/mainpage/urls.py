from django.urls import path, include
from . import views


urlpatterns = [
    # Main
    path('', views.store_page, name='store-page'),

    # Auth
    path('signup/', views.signup_page, name='signup-page'),
    path('login/', views.login_page, name='login-page'),
    path('log-out/', views.logout_page, name='log-out'),
    path('add-to-favorite/<int:product_id>/', views.add_to_favorite, name='add-to-favorite'),
    path('remove-from-favorite/<int:product_id>/', views.remove_from_favorite, name='remove-from-favorite'),
]

