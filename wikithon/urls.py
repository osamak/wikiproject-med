from django.conf.urls import url
from wikithon import views
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

app_name = 'wikithon'
urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='wikithon/index.html'), name='index'),
    #
    url(r'^contact/$', TemplateView.as_view(template_name= 'wikithon/contact.html'), name='contact'),
    #/contact/
    url(r'^about/$', TemplateView.as_view(template_name= 'wikithon/about.html'), name='about'),
    #/about/
    url(r'^sponsor/$', TemplateView.as_view(template_name= 'wikithon/sponsor.html'), name='sponsor'),
    #/sponsor/

    url(r'^wikithons/$', views.ListWikithons.as_view(), name='list_wikithons'),
    #/wikithons/
    url(r'^wikithon/(?P<wikithon_id>[0-9]+)/$', views.ShowWikithon.as_view(), name='show_wikithon'),
    #/wikithons/1/
    url(r'^wikithon/(?P<wikithon_id>[0-9]+)/attendees/$', views.ListAttendees.as_view(), name='list_attendees'),
    #/wikithons/1/attendees

    url(r'^wikithon/add/$', views.AddWikithon.as_view(), name='add_wikithon'),
    #/wikithons/add/
    url(r'^wikithon/(?P<wikithon_id>[0-9]+)/edit/$', views.EditWikithon.as_view(), name='edit_wikithon'),
    #/wikithons/2/update/
    url(r'^wikithon/(?P<wikithon_id>[0-9]+)/delete/$', views.DeleteWikithon.as_view(), name='delete_wikithon'),
    #/wikithons/2/delete

    url(r'^wikithon/(?P<wikithon_id>[0-9]+)/singleinstructions/$', TemplateView.as_view(template_name= 'wikithon/single_instructions.html'), name='single_instructions'),
    #/wikithons/1/singleinstructions/

    url(r'^wikithon/(?P<wikithon_id>[0-9]+)/teaminstructions/$', TemplateView.as_view(template_name= 'wikithon/team_instructions.html'), name='team_instructions'),
    #/wikithons/1/teaminstructions/
    url(r'^wikithon/(?P<wikithon_id>[0-9]+)/creatteam/$', views.CreateTeam.as_view(), name='create_team'),
    #/wikithons/1/creatteam/
    url(r'^wikithon/(?P<wikithon_id>[0-9]+)/team/(?P<team_id>[0-9]+)/$', views.ShowTeam.as_view(), name='show_team'),
    #/wikithons/1/team/1
    url(r'^wikithon/(?P<wikithon_id>[0-9]+)/team/(?P<team_id>[0-9]+)/jointeaminstructions/$', views.JoinTeam.as_view(), name='join_team'),
    #/wikithons/1/team/1/jointeaminstructions



    url(r'^categories/$', views.ListCategories.as_view(), name='list_categories'),
    #/categories/
    url(r'^categories/(?P<category_slug>[0-9]+)/$', views.ShowCategory.as_view(), name='show_category'),
    #/categories/1/

    url(r'^reservationthanks/$', TemplateView.as_view(template_name= 'wikithon/reservation_thanks.html'), name='reservation_thanks'),
    #/reservation_thanks
    url(r'^completionthanks/$', TemplateView.as_view(template_name= 'wikithon/completion_thanks.html'), name='completion_thanks'),
    #/completion_thanks
]
static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)