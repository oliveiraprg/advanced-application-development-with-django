from django.shortcuts import render
from django.views.generic.edit import CreateView
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