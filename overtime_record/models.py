from django.db import models
from collaborators.models import Collaborator


class OvertimeRecord(models.Model):
    reason = models.CharField(max_length=120)
    owner = models.ForeignKey(Collaborator, on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.IntegerField()

    def __str__(self):
        return f'{self.owner}: {self.amount}hrs, reason: {self.reason}'
  