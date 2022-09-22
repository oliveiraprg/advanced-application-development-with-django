from django.db import models
from companys.models import Company
from django.urls import reverse


class Department(models.Model):
    name = models.CharField(max_length=70, verbose_name='Department name')
    company = models.ForeignKey(Company, on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse('departments:list_departments')

    def __str__(self):
        return f'{self.name}'