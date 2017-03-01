from django.db import models

class WikithonQuerySet(models.QuerySet):
    def deleted(self):
        return self.filter(is_deleted=True)

    def undeleted(self):
        return self.filter(is_deleted=False)


class ArticleQuerySet(models.QuerySet):
    def to_user(self, user):
        return self.filter(article_submitter=user)

    def by_user(self, user):
        return self.filter(requester=user)

    def pending(self):
        return self.filter(revisor_status='', reveiwer_status='')

    def canceled(self):
        return self.filter(is_canceled=True)

    def successful(self):
        return ''

    def disputed(self):
        return ''

class GroupQuerySet(WikithonQuerySet):
    def unarchived(self):
        return self.filter(is_archived=False)

    def archived(self):
        return self.filter(is_archived=True)

