from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView
from .models import Company
from django.contrib.auth.mixins import LoginRequiredMixin


class CompanyCreateView(LoginRequiredMixin, CreateView):
    model = Company
    fields = ['name']
    template_name = 'companys/company_create.html'

    def form_valid(self, form):
        obj = form.save() 
        collaborator = self.request.user.collaborator
        collaborator.company = obj
        collaborator.save()
        return HttpResponseRedirect(reverse('core:home'))


class CompanyEditView(LoginRequiredMixin, UpdateView):
    model = Company
    fields = ['name']
    template_name = 'companys/company_update.html'
