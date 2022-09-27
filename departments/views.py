from django.shortcuts import render
from .models import Department
from django.urls import reverse_lazy
from collaborators.models import Collaborator
from django.views.generic import UpdateView, CreateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import DepartmentForm


class DepartmentListView(LoginRequiredMixin, TemplateView):
    template_name = 'departments/department_list.html'

    def get(self, request):
        context = {}
        company = self.request.user.collaborator.company
        collaborator_list = Collaborator.objects.filter(company=company.pk)
        department_list = Department.objects.filter(company=company)
        payroll_list = Collaborator.objects.filter(company=company.pk)
        context['company'] = company
        context['collaborator'] = self.request.user.collaborator
        context['collaborator_list'] = collaborator_list
        context['department_list'] = department_list
        return render(request, self.template_name, context)


class DepartmentCreateView(LoginRequiredMixin, CreateView):
    form_class = DepartmentForm
    template_name = 'departments/department_create.html'

    def form_valid(self, form):
        department = form.save(commit=False)
        company = self.request.user.collaborator.company
        department.company = company
        department.save()
        return super(DepartmentCreateView, self).form_valid(form)


class DepartmentUpdateView(LoginRequiredMixin, UpdateView):
    form_class = DepartmentForm
    template_name = 'departments/department_update.html'


class DepartmentDeleteView(LoginRequiredMixin, DeleteView):
    model = Department
    template_name = 'departments/department_delete.html'
    success_url = reverse_lazy('departments:list_departments')
