from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView
from .models import Company


class CompanyCreateView(CreateView):
    model = Company
    fields = ['name']
    template_name = 'companys/create_company.html'

    def form_valid(self, form):
        obj = form.save() 
        collaborator = self.request.user.collaborator
        collaborator.company = obj
        collaborator.save()
        return HttpResponseRedirect(reverse('core:home'))


class CompanyEditView(UpdateView):
    model = Company
    fields = ['name']
    template_name = 'companys/update_company.html'
