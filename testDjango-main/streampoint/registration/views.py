from django.shortcuts import render, HttpResponsePermanentRedirect, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.urls import reverse
from .forms import UserRegistrationForm, StreamerRegistrationForm, UserLoginForm
from django.contrib.auth.models import Group
from streamers.models import AllStreamers
<<<<<<< Updated upstream
=======
from lkusers.models import ContribUsers
from django.core.exceptions import ObjectDoesNotExist
>>>>>>> Stashed changes


def reg_streamer(request):
    if request.method == 'POST':
        form = StreamerRegistrationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='Streamer')
            user.groups.add(group)
            streamer = AllStreamers.objects.create(streamer=user, name=form.cleaned_data['namestreamer'], urltwitch=form.cleaned_data['twitch_url'], photo=form.cleaned_data['photo'])
            streamer.save()
            return redirect(login)
    else:
        form = StreamerRegistrationForm()
    context = {'form': form}
    return render(request, 'registration/registrstreamer.html', context)


def reg_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
<<<<<<< Updated upstream
=======
            referral_code = request.POST.get('referral_code')
            referred_user = request.user
            try:
                contrib_user = User.objects.get(referral_name=referral_code)
                contrib_user.referral_name = referred_user
                contrib_user.save()
                print("Всё хорошо пользователь найден")
            except ObjectDoesNotExist:
                pass
                print("Ничего не работает")
>>>>>>> Stashed changes
            form.save()
            return redirect('login/')
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'registration/regist.html', context)


def login(requst):
    if requst.method == 'POST':
        form = UserLoginForm(data=requst.POST)
        if form.is_valid():
            username = requst.POST['username']
            password = requst.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(requst, user)
                return redirect('Profile')
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(requst, 'registration/login.html', context)
