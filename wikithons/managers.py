from django.db import models
from django.utils import timezone

class WikithonQuerySet(models.QuerySet):
    def announced(self):
        now = timezone.now()
        return self.filter(announcement_date__lte=now) | \
               self.filter(announcement_date__isnull=True)
