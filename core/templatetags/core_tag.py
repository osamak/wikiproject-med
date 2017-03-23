from django import template
from core import utils

register = template.Library()

@register.filter
def is_organizer(user):
    return utils.is_organizer(user)

@register.filter
def is_reviewer(user):
    return utils.is_reviewer(user)
