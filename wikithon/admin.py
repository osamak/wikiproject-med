from django.contrib import admin
from wikithon.models import Wikithons, Team, Category, Article, Submission
# Register your models here.

admin.site.register(Wikithons)
admin.site.register(Team)
admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Submission)