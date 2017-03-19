from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Wikithon, Team

def list_wikithons(request):
    wikithons = Wikithon.objects.all()
    context = {'wikithons': wikithons}
    return render(request, 'wikithons/list_wikithons.html', context)

def show_wikithon(request, pk):
    wikithon = get_object_or_404(Wikithon, pk=pk)
    context = {'wikithon': wikithon}
    return render(request, 'wikithons/show_wikithon.html', context)

def list_attendees(request, pk):
    wikithon = get_object_or_404(Wikithon, pk=pk)
    if not request.user.is_superuser and \
       not request.user.groups.filter(name="Organizers").exists():
        raise PermissionDenied
    context = {'wikithon': wikithon}
    return render(request, 'wikithons/list_attendees.html', context)

def create_team(request, pk):
    wikithon = get_object_or_404(Wikithon, pk=pk)

    if request.method == 'GET':
        form = TeamForm()
    elif request.method == 'POST':
        instance = Team(founder=request.user)
        form = TeamForm(request.POST, instance=instance)
        if form.is_valid():
            team = form.save()
            url = reverse('wikithons:show_team', args=(team.pk,))
            return HttpResponseRedirect(url)

    context = {'form': form}
    return render(request, 'wikithons/edit_team.html', context)

def edit_team(request, wikithon_pk, pk):
    wikithon = get_object_or_404(Wikithon, pk=pk)

    if request.method == 'GET':
        form = TeamForm()
    elif request.method == 'POST':
        instance = Team(founder=request.user)
        form = TeamForm(request.POST, instance=instance)
        if form.is_valid():
            team = form.save()
            url = reverse('wikithons:show_team', args=(team.pk,))
            return HttpResponseRedirect(url)

    context = {'form': form}
    return render(request, 'wikithons/edit_team.html', context)

def delete_team(request, wikithon_pk, pk):
    pass

def show_team(request, wikithon_pk, pk):
    team = get_object_or_404(Team, wikithon__pk=wikithon_pk, pk=pk)
    context = {'team': team}
    return render(request, 'wikithons/show_team.html', context)

def join_team(request, wikithon_pk, pk, invitation_code):
    team = get_object_or_404(Team, wikithon__pk=wikithon_pk, pk=pk,
                             invitation_code=invitation_code)
    context = {'team': team}
    return render(request, 'wikithons/join_team.html', context)
