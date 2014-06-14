from django.db import models
from registration.models import Manager
# Create your models here.
   

class License(models.Model):
    
    manager = models.ForeignKey(Manager)
    isRenewal = models.BooleanField()
    license_id = models.CharField(max_length=200)
    target_species = models.CharField(max_length=200)
    authorized_zone = models.CharField(max_length=200)
    starting_date = models.DateField()
    issue_date = models.DateField()
    end_date = models.DateField()
    
    