from django.db import models
from django.urls import reverse


class Company(models.Model):
    name = models.CharField(max_length=100, verbose_name='Company Name')

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('core:home')
