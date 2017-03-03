# -*- coding: utf-8  -*-
from django import forms
from django.contrib import admin
from django.contrib.admin.forms import AdminAuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from userena.admin import UserenaAdmin
from accounts.models import Profile

#work on it
#https://docs.djangoproject.com/en/1.10/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_display
#do it again
class UserListAuthenticationForm(AdminAuthenticationForm):
    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise forms.ValidationError(
                self.error_messages['invalid_login'],
                code='invalid_login',
                params={'name': self.name_field.verbose_name}
                )

class UserListAdmin(admin.sites.AdminSite):
    login_form = UserListAuthenticationForm
    def has_permission(self, request):
        return request.user.is_superuser

class ProfileInline(admin.StackedInline):
    model = Profile
    max_num = 1
    extra = 0

def make_active(modeladmin, request, queryset):
    queryset.update(is_active=True)
make_active.short_description = u"نشّط حسابات المساهمين والمساهمات"


class CoordinatorFilter(admin.SimpleListFilter):
    title = u"المنظمين والمنظمات"
    parameter_name = 'is_coordinator'
    def lookups(self, request, model_admin):
        return (
            ('1', u'منظم/ة'),
            ('0', u'ليس منظم/ة'),
        )

    def queryset(self, request, queryset):
        if self.value() == '1':
            return queryset.filter()
        if self.value() == '0':
            return queryset.exclude()

class ReviewerFilter(admin.SimpleListFilter):
    title = u"المراجعين والمراجعات "
    parameter_name = 'is_revirwer'
    def lookups(self, request, model_admin):
        return ''

    def queryset(self, request, queryset):
        # If the filter is actually selected, apply it
        if self.value():
            return queryset.filter()

class ModifiedUserAdmin(UserenaAdmin):

    list_display = ('name', 'email','twitter', 'is_active', 'is_coordinator')
    #'is_revirwer'
    list_filter = (CoordinatorFilter, ReviewerFilter)
    actions = [make_active]
    search_fields= ('name', 'email')
    inlines = [ProfileInline]

    def has_module_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def is_coordinator(self, obj):
        return obj.coordination.current_year().exists()

    is_coordinator.boolean = True
    is_coordinator.short_description =  u'منظم/ة؟'

    def name(self, obj):
        try:
            return obj.profile.get_name()
        except ObjectDoesNotExist:
            return

    def wikithon(self, obj):
        try:
            return obj.profile.get_wikithon()
        except ObjectDoesNotExist:
            return

    def email(self, obj):
        try:
            return obj.profile.email
        except ObjectDoesNotExist:
            return

    def twitter(self, obj):
        try:
            return obj.profile.twitter
        except ObjectDoesNotExist:
            return

    def bio(self, obj):
        try:
            return obj.profile.bio
        except ObjectDoesNotExist:
            return

    name.short_description = u"الاسم"

#user_list_admin = UserListAdmin("User List Admin")
#admin.site.unregister(User)
#admin.site.register(User, ModifiedUserAdmin)
#user_list_admin.register(User, ModifiedUserAdmin)