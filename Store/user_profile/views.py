from django.shortcuts import render, redirect
from .models import UserProfile
from .forms import UserProfileForm


def profile(request):
    try:
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        profile = None

    return render(request, 'user_profile/profile.html', {'profile': profile})


def update_profile(request):
    try:
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        profile = None

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile-view')
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'user_profile/update_profile.html', {'form': form})