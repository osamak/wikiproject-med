from django import template
from django.utils import timezone

register = template.Library()

@register.filter
def has_wikithon_without_article(user):
    today = timezone.now().date()
    return user.registration_set.filter(wikithon__date__gte=today,
                                        articles__isnull=True).exists() or \
           user.teams_founded.filter(wikithon__date__gte=today,
                                     articles__isnull=True).exists()
