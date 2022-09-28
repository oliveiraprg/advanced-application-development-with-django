from django.db import models
from django.contrib.auth.models import User
from departments.models import Department
from companys.models import Company
from django.urls import reverse


class Collaborator(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    salary = models.DecimalField(decimal_places=2, max_digits=15, blank=True, default=0)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    departments = models.ForeignKey(Department, on_delete=models.PROTECT, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.PROTECT, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('collaborators:list_collaborators')
        
    def __str__(self):
        return f'{self.name}'
