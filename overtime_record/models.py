from django.db import models


class OvertimeRecord(models.Model):
    reason = models.CharField(max_length=120)