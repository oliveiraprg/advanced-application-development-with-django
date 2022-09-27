from django.shortcuts import render
from .models import OvertimeWorked
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import OvertimeWorkedForm


class OvertimeWorkedListView(LoginRequiredMixin, TemplateView):
    template_name = 'overtime_worked/overtime_worked_list.html'

    def get(self, request):
        context = {}
        company = self.request.user.collaborator.company
        overtime_worked_list = OvertimeWorked.objects.filter(owner__company=company)
        context['company'] = company
        context['overtime_worked_list'] = overtime_worked_list
        return render(request, self.template_name, context)


class OvertimeWorkedCreateView(LoginRequiredMixin, CreateView):
    template_name = 'overtime_worked/overtime_worked_create.html'
    form_class = OvertimeWorkedForm

    def form_valid(self, form):
        overtime_worked = form.save(commit=False)
        company = self.request.user.collaborator.company
        overtime_worked.company = company
        overtime_worked.save()
        return super(OvertimeWorkedCreateView, self).form_valid(form)


class OvertimeWorkedEditView(LoginRequiredMixin, UpdateView):
    form_class = OvertimeWorkedForm
    template_name = 'overtime_worked/overtime_worked_update.html'


class OvertimeWorkedDeleteView(LoginRequiredMixin, DeleteView):
    model = OvertimeWorked
    template_name = 'overtime_worked/overtime_worked_delete.html'
    success_url = reverse_lazy('overtime_worked:list_overtime_worked')
