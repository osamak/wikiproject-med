# -*- coding: utf-8  -*-
import core.utils

def can_edit_team(user, team):
    if user.is_superuser or team.founder == user \
       or core.utils.is_organizers(user):
        return True
    else:
        return False

def can_view_wikithon_yet(user, wikithon):
    return user.is_superuser or \
        core.utils.is_organizer(user) or \
        wikithon.is_announced()


    
