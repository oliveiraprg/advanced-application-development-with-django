from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=70, verbose_name='Department name')

    def __str__(self):
        return f'{self.name}'