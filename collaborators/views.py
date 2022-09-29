from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView, CreateView, DeleteView, DetailView
from .models import Collaborator
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CollaboratorForm
from random import randint
from django.db.models import Sum, Avg
from django.shortcuts import render


class CollaboratorListView(LoginRequiredMixin, TemplateView):
    template_name = 'collaborators/collaborator_list.html'

    def get(self, request):
        context = {}
        company = self.request.user.collaborator.company
        collaborator_list = Collaborator.objects.filter(company=company.pk)
        payroll_list = {}
        payroll_list['payroll_sum'] = Collaborator.objects.filter(company=company.pk).exclude(status_collaborator='FR').aggregate(Sum('salary'))['salary__sum']
        payroll_list['payroll_avg'] = Collaborator.objects.filter(company=company.pk).exclude(status_collaborator='FR').aggregate(Avg('salary'))['salary__avg']
        context['payroll_list'] = payroll_list
        context['collaborator_list'] = collaborator_list
        context['company'] = company
        print(context)
        print('caralho')
        return render(request, self.template_name, context)


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
