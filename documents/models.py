from django.db import models
from collaborators.models import Collaborator
from companys.models import Company


class Document(models.Model):
    file_name = models.CharField(max_length=100)
    owner = models.ForeignKey(Collaborator, on_delete=models.SET_NULL, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    
    def __str__(self):
        return f'{self.file_name} - {self.owner}'
