from django.db import models
from companys.models import Company
from django.urls import reverse
from django.db.models import Sum


class Department(models.Model):
    name = models.CharField(max_length=70, verbose_name='Department name')
    company = models.ForeignKey(Company, on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse('departments:list_departments')

    @property
    def total_payroll(self):
        payroll = self.collaborator_set.exclude(status_collaborator='FR').aggregate(Sum('salary'))['salary__sum']
        return payroll or 0

    def __str__(self):
        return f'{self.name}'