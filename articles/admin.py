from django.contrib import admin
from .models import Category, Article, Reservation

admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Reservation)
