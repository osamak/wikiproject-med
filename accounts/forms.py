# -*- coding: utf-8  -*-
from django import forms
from userena.forms import SignupForm
from accounts.models import Profile

class WikithonSignupForm(SignupForm):
    name = forms.CharField(label=Profile._meta.get_field('name').verbose_name,
                            max_length=100)
    email = forms.EmailField(label=Profile._meta.get_field('email').verbose_name)
    twitter = forms.CharField(label=Profile._meta.get_field('twitter').verbose_name,
                              max_length=20)
    bio = forms.TextField(label=Profile._meta.get_field('bio').verbose_name, widget=forms.Textarea)
    avatar = forms.ImageField(label=Profile._meta.get_field('avatar').verbose_name)

    def save(self):
        # Save the parent form and get the user
        new_user = super(WikithonSignupForm, self).save()

        Profile.objects.create(user=new_user,
                               name=self.cleaned_data['name'],
                               email=self.cleaned_data['email'],
                               twitter=self.cleaned_data['twitter'],
                               bio=self.cleaned_data['bio'],
                               avatar=self.cleaned_data['avatar'])

        return new_user

class EditProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email', 'twitter','bio', 'avatar']

class ResendForm(forms.Form):
    email = forms.EmailField()
