from django.db import models
from django.contrib.auth.models import User
from departments.models import Department
from companys.models import Company


class Collaborator(models.Model):
    name = models.CharField(max_length=100, verbose_name='Collaborator Name')
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    departments = models.ManyToManyField(Department)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.name} - {self.company}'
