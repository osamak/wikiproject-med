from django.conf.urls import url
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from articles import views

urlpatterns = [
    url(r'^$', views.list_categories, name='list_categories'),
    url(r'^categories/$', RedirectView.as_view(pattern_name="articles:list_categories")),
    url(r'^categories/(?P<slug>[\d\w_]+)/$', views.show_category, name='show_category'),
    url(r'^reservationthanks/$', TemplateView.as_view(template_name= 'wikithon/reservation_thanks.html'), name='reservation_thanks'),
    url(r'^completionthanks/$', TemplateView.as_view(template_name= 'wikithon/completion_thanks.html'), name='completion_thanks'),
]
