from django.conf.urls.static import static
from django.urls import path
from . import views
from Store import settings

urlpatterns = [
    path('settings/', views.settings_view, name='settings'),

    path('settings/appearance/', views.appearance_settings_view, name='appearance-settings'),

    path('settings/confidentiality/', views.confidentiality_settings_view, name='confidentiality-settings'),
    path('settings/confidentiality/change-password/', views.change_password, name='change-password'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)