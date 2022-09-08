from django.db import models


class Document(models.Model):
    file_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.file_name}'