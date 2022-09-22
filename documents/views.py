from django.shortcuts import render
from collaborators.models import Collaborator
from .models import Document
from django.views.generic import UpdateView, CreateView, DeleteView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class DocumentListView(LoginRequiredMixin, TemplateView):
    template_name = 'documents/document_list.html'

    def get(self, request):
        context = {}
        company = self.request.user.collaborator.company
        collaborator_list = Collaborator.objects.filter(company=company.pk)
        document_list = Document.objects.filter(company=company)
        context['company'] = company
        context['collaborator'] = self.request.user.collaborator
        context['collaborator_list'] = collaborator_list
        context['document_list'] = document_list
        return render(request, self.template_name, context)


class DocumentCreateView(LoginRequiredMixin, CreateView):
    model = Document
    fields = ['file_name', 'document_file']
    template_name = 'documents/document_create.html'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        collaborator = Collaborator.objects.get(pk=self.kwargs['collaborator_id']) 
        company = self.request.user.collaborator.company
        form.instance.owner_id = collaborator.pk
        form.instance.company_id = company.pk
        
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class DocumentEditView(LoginRequiredMixin, UpdateView):
    model = Document
    fields = ['file_name', 'document_file']
    template_name = 'documents/document_update.html'


class DocumentDeleteView(LoginRequiredMixin, DeleteView):
    model = Document
    template_name = 'documents/document_delete.html'
    success_url = reverse_lazy('documents:list_documents')

