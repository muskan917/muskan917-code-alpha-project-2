from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Profile

def user_profile(request, username):
    user = User.objects.get(username=username)
    profile = Profile.objects.get(user=user)
    return render(request, 'user_profile.html', {'profile': profile})

def follow_user(request, username):
    user_to_follow = User.objects.get(username=username)
    profile = Profile.objects.get(user=user_to_follow)
    if request.user in profile.followers.all():
        profile.followers.remove(request.user)
    else:
        profile.followers.add(request.user)
    return redirect('user-profile', username=user_to_follow.username)
