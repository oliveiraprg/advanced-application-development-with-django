from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView
from .models import Collaborator
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CollaboratorForm
from random import randint


class CollaboratorListView(LoginRequiredMixin, ListView):
    model = Collaborator
    
    def get_queryset(self):
        company = self.request.user.collaborator.company
        collaborator_list = Collaborator.objects.filter(company=company.pk)
        return collaborator_list


class CollaboratorCreateView(LoginRequiredMixin, CreateView):
    form_class = CollaboratorForm
    template_name = 'collaborators/collaborator_create.html'

    def form_valid(self, form):
        collaborator = form.save(commit=False)
        company = self.request.user.collaborator.company
        collaborator.company = company
        username_collaborator = str(collaborator.name.split(' ')[0] + collaborator.name.split(' ')[-1]).lower()
        if User.objects.filter(username=username_collaborator).exists():
            username_collaborator = username_collaborator + str(randint(1, 99))
        collaborator.user = User.objects.create(username=username_collaborator)
        collaborator.save()
        return super(CollaboratorCreateView, self).form_valid(form)
    
    def get_form_kwargs(self) :
        kwargs = super(CollaboratorCreateView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class CollaboratorEditView(LoginRequiredMixin, UpdateView):
    model = Collaborator
    form_class = CollaboratorForm
    template_name = 'collaborators/collaborator_update.html'
    
    def get_form_kwargs(self) :
        kwargs = super(CollaboratorEditView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class CollaboratorDeleteView(LoginRequiredMixin, DeleteView):
    model = Collaborator
    template_name = 'collaborators/collaborator_delete.html'
    success_url = reverse_lazy('collaborators:list_collaborators')


class CollaboratorDetailView(DetailView):
    model = Collaborator
    template_name = 'collaborators/collaborator_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
