# -*- coding: utf-8  -*-
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages

from .forms import ResendForm
from .models import Profile
from userena.models import UserenaSignup


def resend_confirmation_key(request):
    if request.method == 'POST':
        form = ResendForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                user = User.objects.get(email__iexact=email)
                userena_signup = user.userena_signup
            except User.DoesNotExist:
                context = {"error": u"nonexistent"}
                return render(request, 'accounts/resend_confirmation_code.html', context)

            if user.is_active:
                context = {"error": "already_active"}
                return render(request, 'accounts/resend_confirmation_code.html', context)

            new_key = UserenaSignup.objects.reissue_activation(userena_signup.activation_key)
            if new_key:
                return render(request, 'userena/activate_retry_success.html')
        else:
            context = {"form": form}
            return render(request, 'accounts/resend_confirmation_code.html', context)

    elif request.method == 'GET':
        return render(request, 'accounts/resend_confirmation_code.html')

def edit_profile(request):
    try:
        profile = request.user.profile
    except ObjectDoesNotExist:
        return HttpResponseRedirect(reverse('home'))

    if request.method == 'POST':
        form = Profile(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'تم تعديل بياناتك بنجاح')
            return HttpResponseRedirect(reverse('edit_profile'))
    elif request.method == 'GET':
        form = Profile(instance=profile)

    return render(request, 'accounts/edit_profile.html', {'form': form, 'profile': profile})
