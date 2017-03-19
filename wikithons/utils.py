# -*- coding: utf-8  -*-
import datetime
from django.utils import timezone
import accounts.utils


def create_tweet(user, action):
    if not user.social_auth.exists():
            return
    elif action == "coming_to_wikithon":
        text = u"سجلت في ويكيثون  {}!\nيمكن الانضمام الآن: {}"
    elif action == "booked_article":
        text = u" ساترجم المقالة {}!\nيمكن الانضمام الآن: {}"
    elif action == "create_team":
        text = u"اسست فريق  {}!\nيمكن الانضمام الآن: {}"
    elif action == "joined_team":
        text = u"انضممت لفريق  {}!\nيمكن الانضمام الآن: {}"


def is_coordinator(user):
    coordinator = accounts.utils.get_user_coordination_and_deputyships(user)
    return coordinator.filter().exists()

def is_reviewer(user):
    reviewer = accounts.utils.get_user_coordination_and_deputyships(user)
    return reviewer.filter().exists()

def can_edit_wikithon(user, wikithon):
    return is_coordinator(user) or user.is_superuser

def can_edit_article_status(user, article):
    return is_coordinator(user) or user.is_superuser
           #user.is_reviewer(don't know how to add it)

def can_attend_wikithon(user, wikithon):
    wikithon_datetime = timezone.make_aware(datetime.datetime.combine(wikithon.date, wikithon.start_time), timezone.get_default_timezone())
    if wikithon.is_deleted or \
       timezone.now() > wikithon_datetime or \
       wikithon.confirmed_attendees.filter(pk=user.pk).exists() :
        return False
    else:
        return True

#def get_article_submitted(article):
    #return (didn't know what should I do)

def can_edit_user_profile(user, user_profile):
    return is_coordinator(user) or \
       user.is_superuser or \
       user_profile.user == user

def is_active_group_member(user, group):
    return group.membership_set.filter(user=user, is_active=True).exists()

def can_edit_group(user, group):
    return is_coordinator(user) or \
       user.is_superuser or \
       group.coordinator == user

def can_join_group(user, group):
    if group.is_deleted or \
       group.is_archived or \
       group.membership_set.filter(user=user).exists() or \
       group.coordinator == user :
        return False
    else:
        return True


