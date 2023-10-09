from django.contrib.auth import update_session_auth_hash
from django.core.checks import messages
from django.shortcuts import render, redirect
from .models import UserProfile
from .forms import AppearanceSettingsForm, ConfidentialitySettingsForm, ChangePasswordForm


def settings_view(request):
    selected_setting = request.GET.get('setting')
    filtered_profiles = UserProfile.objects.all()

    if selected_setting:
        filtered_profiles = filtered_profiles.filter(setting__name=selected_setting)

    return render(request, 'user_settings/settings.html', {
        'profiles': filtered_profiles,
        'selected_setting': selected_setting,
    })


def appearance_settings_view(request):
    if request.method == 'POST':
        appearance_settings_form = AppearanceSettingsForm(request.POST)
        if appearance_settings_form.is_valid():
            pass
    else:
        appearance_settings_form = AppearanceSettingsForm()

    return render(request, 'appearance_settings.html', {'appearance_settings_form': appearance_settings_form})


def confidentiality_settings_view(request):
    if request.method == 'POST':
        confidentiality_settings_form = ConfidentialitySettingsForm(request.POST)
        if confidentiality_settings_form.is_valid():
            pass
    else:
        confidentiality_settings_form = ConfidentialitySettingsForm()

    return render(request, 'confidentiality_settings.html', {'confidentiality_settings_form': confidentiality_settings_form})


def change_password(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            current_password = form.cleaned_data['current_password']
            new_password1 = form.cleaned_data['new_password1']
            new_password2 = form.cleaned_data['new_password2']

            if not request.user.check_password(current_password):
                messages.error(request, 'Invalid current password.')
            else:
                if new_password1 == new_password2:
                    request.user.set_password(new_password1)
                    request.user.save()
                    update_session_auth_hash(request, request.user)
                    messages.success(request, 'Your password was successfully changed.')
                    return redirect('confidentiality-settings')
                else:
                    messages.error(request, 'New passwords do not match.')
    else:
        form = ChangePasswordForm()

    return render(request, 'change_password.html', {'form': form})