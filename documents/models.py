from django.db import models
from collaborators.models import Collaborator


class Document(models.Model):
    file_name = models.CharField(max_length=100)
    owner = models.ForeignKey(Collaborator, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.file_name} - {self.owner}'
