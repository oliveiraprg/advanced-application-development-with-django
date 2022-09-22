from collaborators.models import Collaborator
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "core/index.html"

    def get_queryset(self):
        context = {}
        company = self.request.user.collaborator.company
        collaborator_list = Collaborator.objects.filter(company=company.pk)
        context['company'] = company 
        context['collaborator_list'] = collaborator_list
        context['collaborator'] = self.request.user.collaborator
        context['user'] = self.request.user
        return context