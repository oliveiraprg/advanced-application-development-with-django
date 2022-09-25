from django.db import models
from collaborators.models import Collaborator
from django.urls import reverse


class OvertimeWorked(models.Model):
    reason = models.CharField(max_length=120)
    owner = models.ForeignKey(Collaborator, on_delete=models.SET_NULL, null=True, blank=True)
    amount_hours = models.DecimalField(max_digits=5, decimal_places=2)

    def get_absolute_url(self):
        return reverse('overtime_worked:list_overtime_worked')

    def __str__(self):
        return f'{self.owner}: {self.amount_hours}hrs, reason: {self.reason}'
  