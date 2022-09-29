from django.db import models
from django.contrib.auth.models import User
from departments.models import Department
from companys.models import Company
from django.urls import reverse
from django.utils.timezone import now


ON_VACATION = 'VC'
FIRED = 'FR'
ACTIVE = 'AT'
AWAY = 'AW'
COLLABORATOR_STATUS_CHOICES = [
    (ON_VACATION, 'ON VACATION'),
    (FIRED, 'FIRED'),
    (ACTIVE, 'ACTIVE'),
    (AWAY, 'AWAY FROM WORK'),
]
class Collaborator(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    salary = models.DecimalField(decimal_places=2, max_digits=15, blank=True, default=0)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    start_in_company = models.DateField(default=now)
    fired_of_company = models.DateField(null=True, blank=True)
    status_collaborator = models.CharField(
        max_length=2,
        choices=COLLABORATOR_STATUS_CHOICES,
        default=ACTIVE,
    )
    departments = models.ForeignKey(Department, on_delete=models.PROTECT, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.PROTECT, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('collaborators:list_collaborators')
        
    def __str__(self):
        return f'{self.name}'
