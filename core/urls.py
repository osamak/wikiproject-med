from django.conf.urls import url
from django.views.generic import TemplateView
from core import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^contact/$', TemplateView.as_view(template_name= 'contact.html'), name='contact'),
    url(r'^charter/$', TemplateView.as_view(template_name= 'charter.html'), name='charter'),
    url(r'^about/$', TemplateView.as_view(template_name= 'about.html'), name='about'),
    url(r'^sponsor/$', TemplateView.as_view(template_name= 'sponsor.html'), name='sponsor'),
]
