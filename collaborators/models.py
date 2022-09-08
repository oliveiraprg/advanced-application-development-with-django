from django.db import models


class Collaborator(models.Model):
    name = models.CharField(max_length=100, verbose_name='Collaborator Name')

    def __str__(self):
        return f'{self.name}'
