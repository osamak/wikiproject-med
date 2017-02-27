# -*- coding: utf-8  -*-
from django import forms
from userena.forms import SignupForm
from accounts.models import Profile

class WikithonSignupForm(SignupForm):
    name = forms.CharField(label=Profile._meta.get_field('الاسم').verbose_name,
                                max_length=30)
    email = forms.EmailField(label=Profile._meta.get_field(' البريد الإلكتروني').verbose_name,
                                max_length=30)
    twitter = forms.CharField(label=Profile._meta.get_field('حساب تويتر').verbose_name,
                                max_length=30)
    bio = forms.CharField(label=Profile._meta.get_field('الوصف').verbose_name,
                                max_length=30)
    avatar = forms.ImageField(label=Profile._meta.get_field('الصورة الشخصية').verbose_name,
                                max_length=30)

    def save(self):
        # Save the parent form and get the user
        new_user = super(WikithonSignupForm, self).save()

        Profile.objects.create(user=new_user,
                                     name=self.cleaned_data['الاسم'],
                                     email=self.cleaned_data[' البريد الإلكتروني'],
                                     twitter=self.cleaned_data['حساب تويتر'],
                                     bio=self.cleaned_data['الوصف'],
                                     avatar=self.cleaned_data['الصورةالشخصية'],
                                    )

        return new_user

class EditWikithonProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email', 'twitter','bio', 'avatar']
    def clean(self):
        cleaned_data = super(EditWikithonProfile, self).clean()

        return cleaned_data

    def save(self):
        profile = super(EditWikithonProfile, self).save()
        profile.save()

class ResendForm(forms.Form):
    email = forms.EmailField()