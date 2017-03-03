from django.views import generic
from wikithon.models import Wikithons, Team, Category, Article
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
import string
import random


class IndexView(generic.TemplateView):
    template_name = 'wikithon/index.html'
    context_object_name = 'all_categories'
    def get_queryset(self):
        return Category.objects.all()

class ContactView(generic.TemplateView):
    template_name = 'wikithon/contact.html'
class AboutView(generic.TemplateView):
    template_name = 'wikithon/about.html'
class SponsorView(generic.TemplateView):
    template_name = 'wikithon/sponsor.html'

class ListWikithons(generic.ListView):
    template_name = 'wikithon/list_wikithons.html'
    context_object_name = "wikithon"
    def get_queryset(self):
        return Wikithons.objects.all()


class ShowWikithon(generic.DetailView):
    model = Wikithons
    template_name = 'wikithon/show_wikithons.html'
    context_object_name = "Wikithons"
    pk_url_kwarg = "wikithons_id"
    query_pk_and_slug = True

class ListAttendees(generic.ListView):
    template_name = 'wikithon/list_attendees.html'
    context_object_name = "attendees"
    def get_queryset(self):
        return Team.objects.all()

class AddWikithon(CreateView):
    model = Wikithons
    fields = ['name','description', 'date_time', 'duration', 'location' ]
    success_url = reverse_lazy('wikithon:index')
    template_name = 'wikithon/add_wikithon.html'
    pk_url_kwarg = "wikithons_id"
    query_pk_and_slug = True
class EditWikithon(UpdateView):
    model = Wikithons
    fields = ['name','description', 'date_time', 'duration', 'location' ]
    success_url = reverse_lazy('wikithon:index')
    pk_url_kwarg = "wikithons_id"
    query_pk_and_slug = True
class DeleteWikithon(DeleteView):
    model = Wikithons
    success_url = reverse_lazy('project:index')
    pk_url_kwarg = "wikithons_id"
    query_pk_and_slug = True


class SingleInstructions(generic.TemplateView):
    template_name = 'wikithon/single_instructions.html'

class TeamInstructions(generic.TemplateView):
    template_name = 'wikithon/team_instructions.html'
    success_url = reverse_lazy('wikithon:create_team')
class CreateTeam(CreateView):
    model = Team
    fields = ['name', 'logo', 'description' ]
    success_url = reverse_lazy('wikithon:show_team')
    pk_url_kwarg = "team_id"
    query_pk_and_slug = True
    def form_valid(self, form):
        form.instance.founder = self.request.user
        return super(CreateTeam, self).form_valid(form)
    def form_valid(self, form):
        invitation_code = ""
        for i in range(10):
            invitation_code += random.choice(string.uppercase + string.digits + string.lowercase)
        form.instance.invitation_code = invitation_code
        return super(CreateTeam, self).form_valid(form)
#link to wikithon

class ShowTeam(generic.DetailView):
    model = Team
    template_name = 'wikithon/show_team.html'
    context_object_name = "team"
    pk_url_kwarg = "team_id"
    query_pk_and_slug = True
class JoinTeam(generic.DetailView):
    template_name = 'wikithon/join_team.html'
    success_url = reverse_lazy('wikithon:show_team')


class ListCategories(generic.ListView):
    template_name = 'wikithon/list_categories.html'
    context_object_name = "categories"
    def get_queryset(self):
        return Category.objects.all()

class ShowCategory(generic.DetailView):
    model = Article
    template_name = 'wikithon/show_category.html'
    context_object_name = "articles"
    pk_url_kwarg = "category_slug"
    query_pk_and_slug = True
    def get_queryset(self):
        return Article.objects.all()

class ReservationThanksView(generic.TemplateView):
    template_name = 'wikithon/reservation_thanks.html'
class CompletionThanksView(generic.TemplateView):
    template_name = 'wikithon/completion_thanks.html'
