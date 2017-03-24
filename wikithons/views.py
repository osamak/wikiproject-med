# -*- coding: utf-8  -*-
from core import decorators
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from wikithons import utils
from .models import Wikithon, Team
import core.utils


def list_wikithons(request):
    wikithons = Wikithon.objects.announced()
    today = timezone.now().date()
    next_wikithon = Wikithon.objects.announced().filter(date__gte=today).order_by("date").first()
    context = {'wikithons': wikithons,
               'next_wikithon': next_wikithon}
    return render(request, 'wikithons/list_wikithons.html', context)

def show_wikithon(request, pk):
    wikithon = get_object_or_404(Wikithon, pk=pk)

    if not utils.can_view_wikithon_yet(request.user, wikithon):
        raise Http404
    
    context = {'wikithon': wikithon}
    return render(request, 'wikithons/show_wikithon.html', context)

@login_required
def list_attendees(request, pk):
    wikithon = get_object_or_404(Wikithon, pk=pk)
    if not request.user.is_superuser and \
       not core.utils.is_organizer(request.user):
        raise PermissionDenied
    context = {'wikithon': wikithon}
    return render(request, 'wikithons/list_attendees.html', context)

@decorators.ajax_only
@login_required
def create_team(request, pk):
    wikithon = get_object_or_404(Wikithon, pk=pk)

    if not utils.can_view_wikithon_yet(request.user, wikithon):
        raise Http404

    if request.method == 'GET':
        form = TeamForm()
    elif request.method == 'POST':
        instance = Team(founder=request.user)
        form = TeamForm(request.POST, instance=instance)
        if form.is_valid():
            team = form.save()
            url = reverse('wikithons:show_team', args=(pk, team.pk,))
            return {'show_url': url}

    context = {'form': form}
    return render(request, 'wikithons/edit_team.html', context)

@decorators.ajax_only
@login_required
def edit_team(request, wikithon_pk, pk):
    team = get_object_or_404(team, wikithon__pk=wikithon_pk, pk=pk)

    if not utils.can_edit_team(request.user, team):
        raise Exception("لا يمكنك تعديل الفريق")

    if request.method == 'GET':
        form = TeamForm(instance=team)
    elif request.method == 'POST':
        form = TeamForm(request.POST, instance=team)
        if form.is_valid():
            team = form.save()
            url = reverse('wikithons:show_team', args=(wikithon_pk, team.pk,))
            return {'show_url': url}

    context = {'form': form}
    return render(request, 'wikithons/edit_team.html', context)

@decorators.ajax_only
@login_required
def delete_team(request, wikithon_pk, pk):
    team = get_object_or_404(team, wikithon__pk=wikithon_pk, pk=pk)

    if not utils.can_edit_team(request.user, team):
        raise Exception("لا يمكنك حذف الفريق")

    if team.is_deleted:
        raise Exception("الفريق محذوف فعلا")
    team.is_deleted = True
    team.save()

    url = reverse('wikithons:show_wikithon', args=(wikithon_pk,))
    return {'show_url': url}

def show_team(request, wikithon_pk, pk):
    team = get_object_or_404(Team, wikithon__pk=wikithon_pk, pk=pk)
    context = {'team': team}
    return render(request, 'wikithons/show_team.html', context)

@decorators.ajax_only
@login_required
def toggle_join_team(request, wikithon_pk, pk, invitation_code):
    team = get_object_or_404(Team, wikithon__pk=wikithon_pk, pk=pk,
                             invitation_code=invitation_code)
    action = request.POST.get('action')
    

    if team.founder == request.user:
        raise Exception("لا يمكن إتمام عضوية")
    if action == 'join':
        if team.members.filter(pk=request.user.pk).exists():
            raise Exception("لديك عضوية الفريق فعلا")
        team.members.add(request.user)
    elif action == 'leave':
        if not team.members.filter(pk=request.user.pk).exists():
            raise Exception("ليس لديك عضوية في الفريق")
        team.members.remove(request.user)

    return {}

@login_required
def show_join_team_introduction(request, wikithon_pk, pk, invitation_code):
    team = get_object_or_404(Team, wikithon__pk=wikithon_pk, pk=pk,
                             invitation_code=invitation_code)
    context = {'team': team}
    return render(request, 'wikithons/edit_team.html', context)

@decorators.ajax_only
@login_required
def toggle_registration(request, pk):
    wikithon = get_object_or_404(Wikithon, pk=pk)

    if not wikithon.is_announced():
        raise Http404

    action = request.POST.get('action')
    registration =  Registration.objects.filter(wikithon=wikithon).first()

    if action  == 'register':
        if registration and not registration.is_deleted:
            raise Exception("سبق التسجيل!")
        elif registration and registration.is_deleted:
            registration.is_deleted = False
            registration.save()
        else:
            Registration.objects.create(user=request.user,
                                        wikithon=wikithon)
    elif action  == 'unregister':
        if not registration or registration.is_deleted:
            raise Exception("لم يسبق لك التسجيل")
        elif registration and not registration.is_deleted:
            registration.is_deleted = True
            registration.save()

    return {}
