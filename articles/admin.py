from django.contrib import admin
from .models import Category, Article, Reservation

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'get_article_count']

class ReservationInline(admin.TabularInline):
    model = Reservation
    extra = 0
    
class ArticleAdmin(admin.ModelAdmin):
    search_fields = ['en_name', 'ar_name']
    list_display = ['en_name', 'ar_name']
    list_filter = ['category', 'is_available']
    inlines = [ReservationInline]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)

