from django.db import models

class ArticleQuerySet(models.QuerySet):
    def to_user(self, user):
        return self.filter(article_submitter=user)
    def by_user(self, user):
        return self.filter(requester=user)

    def make_reserved(modeladmin, request, queryset):
        queryset.update(status='RES')
    def make_submitted(modeladmin, request, queryset):
        queryset.update(status='SUB')
    def make_published(modeladmin, request, queryset):
        queryset.update(status='PUB')
    def make_rejected(modeladmin, request, queryset):
        queryset.update(status='REJ')