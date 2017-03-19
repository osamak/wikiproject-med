from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', views.list_wikithons, name='list_wikithons'),
    url(r'^(?P<pk>\d+)/$', views.show_wikithon, name='show_wikithon'),
    url(r'^(?P<pk>\d+)/attendees/$', views.list_attendees, name='list_attendees'),
    url(r'^(?P<pk>\d+)/singleinstructions/$', TemplateView.as_view(template_name= 'wikithon/single_instructions.html'), name='single_instructions'),
    url(r'^(?P<pk>\d+)/teaminstructions/$', TemplateView.as_view(template_name= 'wikithon/team_instructions.html'), name='team_instructions'),
    url(r'^(?P<pk>\d+)/create-team/$', views.create_team, name='create_team'),
    url(r'^(?P<wikithon_pk>\d+)/team/(?P<pk>\d+)/$', views.show_team, name='show_team'),
    url(r'^(?P<wikithon_pk>\d+)/team/(?P<pk>\d+)/edit/$', views.edit_team, name='edit_team'),
    url(r'^(?P<wikithon_pk>\d+)/team/(?P<pk>\d+)/delete/$', views.delete_team, name='delete_team'),
    url(r'^(?P<wikithon_pk>\d+)/team/(?P<pk>\d+)/(?P<invitation_code>[\d\w]+)/$', views.join_team, name='join_team'),
]
