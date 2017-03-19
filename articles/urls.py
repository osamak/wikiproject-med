from django.conf.urls import url
from django.views.generic import TemplateView
from articles import views

urlpatterns = [
    url(r'^categories/$', views.ListCategories.as_view(), name='list_categories'),
    url(r'^categories/(?P<slug>[\d\w_]+)/$', views.show_category, name='show_category'),
    url(r'^reservationthanks/$', TemplateView.as_view(template_name= 'wikithon/reservation_thanks.html'), name='reservation_thanks'),
    url(r'^completionthanks/$', TemplateView.as_view(template_name= 'wikithon/completion_thanks.html'), name='completion_thanks'),
]
