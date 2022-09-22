from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from .models import Collaborator
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin


class CollaboratorListView(LoginRequiredMixin, ListView):
    model = Collaborator
    paginate_by = 25
    
    def get_queryset(self):
        company = self.request.user.collaborator.company
        collaborator_list = Collaborator.objects.filter(company=company.pk)
        return collaborator_list


class CollaboratorCreateView(LoginRequiredMixin, CreateView):
    model = Collaborator
    fields = ['name']
    template_name = 'collaborators/collaborator_create.html'

    def form_valid(self, form):
        collaborator = form.save(commit=False)
        company = self.request.user.collaborator.company
        collaborator.company = company
        username_collaborator = str(collaborator.name.split(' ')[0] + collaborator.name.split(' ')[-1]).lower()
        collaborator.user = User.objects.create(username=username_collaborator)
        collaborator.save()
        return super(CollaboratorCreateView, self).form_valid(form)


class CollaboratorEditView(LoginRequiredMixin, UpdateView):
    model = Collaborator
    fields = ['name', 'departments']
    template_name = 'collaborators/collaborator_update.html'


class CollaboratorDeleteView(LoginRequiredMixin, DeleteView):
    model = Collaborator
    template_name = 'collaborators/collaborator_delete.html'
    success_url = reverse_lazy('collaborators:list_collaborators')
