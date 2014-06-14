from django.db import models

# Create your models here.
class Report(models.Model):
    id_of_canoe = models.CharField(max_length=32)
    investigated = models.BooleanField()