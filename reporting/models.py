from django.db import models

# Create your models here.
class Report(models.Model):
    canoe_id = models.IntegerField()
    
    def __unicode__(self):
        return self.canoe_id
    
#compliance form not available to only fishing authorities
class Compliance(models.Model):
    canoe = models.OneToOneField(Report, primary_key = True)
    inspection_id = models.IntegerField()
    id_canoe = models.IntegerField()
    inspection_authority = models.CharField(max_length=200)
    officer_name = models.CharField(max_length=200)
    inspection_date = models.DateField()
    inspection_time = models.TimeField()
    inspection_place = models.CharField(max_length=200)
    gps_coordinate = models.DecimalField(max_digits=6,decimal_places=3)
    is_compliant = models.BooleanField() #passed inspection?
    volume_fish_confiscated = models.DecimalField(max_digits=6, decimal_places=3)
    nature_of_offense = models.CharField(max_length=500)
    expected_sanction = models.CharField(max_length=500)
    final_decision = models.CharField(max_length=500)
    name_of_authority = models.CharField(max_length=200)
    date = models.DateField()
    
    def __unicode__(self):
        return self.id_canoe

    