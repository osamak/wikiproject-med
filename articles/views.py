from django.shortcuts import render, get_object_or_404
from .models import Category, Article

def list_categories(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'articles/list_categories.html', context)

def show_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    context = {'category': category}
    return render(request, 'articles/show_category.html', context)
