# -*- coding: utf-8  -*-
"""
Utility functions for the accounts app.
"""
from django.core.exceptions import ObjectDoesNotExist

def get_user_profile_type(user):

    if not user.is_authenticated() or \
       user.is_superuser:
        return ''

    # If the profile is absent, return None.
    try:
        profile_type = user.Profile
    except (ObjectDoesNotExist, AttributeError):
        profile_type = ''

    return profile_type