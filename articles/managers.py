from django.db import models

class ArticleQuerySet(models.QuerySet):
    def available(self):
        return self.filter(is_available=True)
