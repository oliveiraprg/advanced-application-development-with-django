from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from collaborators.models import Collaborator


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "core/index.html"

    def get(self, request):
        context = {}
        if self.request.user.collaborator.company:
            company = self.request.user.collaborator.company
            collaborator_list = Collaborator.objects.filter(company=company.pk)
        else:
            company = None
            collaborator_list = None
        context['company'] = company 
        context['collaborator'] = self.request.user.collaborator
        context['collaborator_list'] = collaborator_list
        return render(request, self.template_name, context)
