from django.conf.urls import url
from wikithon import views

app_name = 'wikithon'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    #/
    url(r'^home/$', views.IndexView.as_view(), name='home'),
    #/home/



    url(r'^wikithons/$', views.ListWikithons.as_view(), name='list_wikithons'),
    #/wikithons/
    url(r'^wikithon/(?P<wikithon_id>[0-9]+)/$', views.ShowWikithon.as_view(), name='show_wikithon'),
    #/wikithons/1/
    url(r'^wikithon/(?P<wikithon_id>[0-9]+)/attendees/$', views.ListAttendees.as_view(), name='list_attendees'),
    #/wikithons/1/attendees

    url(r'^wikithon/add/$', views.AddWikithon.as_view(), name='add_wikithon'),
    #/wikithon/add/
    url(r'^wikithon/(?P<wikithon_id>[0-9]+)/edit/$', views.EditWikithon.as_view(), name='edit_wikithon'),
    #/wikithon/2/update/
    url(r'^wikithon/(?P<wikithon_id>[0-9]+)/delete/$', views.DeleteWikithon.as_view(), name='delete_wikithon'),
    #/wikithon/2/delete

    url(r'^wikithon/(?P<wikithon_id>[0-9]+)/singleinstructions/$', views.SingleInstructions.as_view(), name='single_instructions'),
    #/wikithons/1/singleinstructions/

    url(r'^wikithon/(?P<wikithon_id>[0-9]+)/teaminstructions/$', views.TeamInstructions.as_view(), name='team_instructions'),
    #/wikithons/1/teaminstructions/
    url(r'^wikithon/(?P<wikithon_id>[0-9]+)/creatteam/$', views.CreateTeam.as_view(), name='create_team'),
    #/wikithons/1/creatteam/
    url(r'^wikithon/(?P<wikithon_id>[0-9]+)/team/(?P<team_id>[0-9]+)/$', views.ShowTeam.as_view(), name='show_team'),
    #/wikithons/1/team/1
    url(r'^wikithon/(?P<wikithon_id>[0-9]+)/team/(?P<team_id>[0-9]+)/jointeaminstructions/$', views.JoinTeam.as_view(), name='join_team'),
    #/wikithons/1/team/1/jointeaminstructions



    url(r'^categories/$', views.ListCategories.as_view(), name='list_categories'),
    #/categories/
    url(r'^categories/(?P<category_id>[0-9]+)/$', views.ShowCategory.as_view(), name='show_category'),
    #/categories/1/

    url(r'^reservationthanks/$', views.ReservationThanksView.as_view(), name='reservation_thanks'),
    #/reservation_thanks
    url(r'^completionthanks/$', views.CompletionThanksView.as_view(), name='completion_thanks'),
    #/completion_thanks
]