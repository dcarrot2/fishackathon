from django.db import models

#Registration of canoes
class Manager(models.Model):
    name_of_fisher = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1)
    occupation = models.CharField(max_length=200)
    phone_number = models.IntegerField()
    manager_address = models.CharField(max_length=200)
    number_of_canoes = models.IntegerField()
    
    hull_material = models.CharField(max_length=200)
    vessel_size = models.DecimalField(max_digits=10, decimal_places=3)
    
    def __unicode(self):
        return self.name_of_fisher
    


class Canoe(models.Model):
    owner = models.ForeignKey(Manager)
    current_canoe_number = models.IntegerField()
    coastal_region = models.CharField(max_length=100)
    coastal_district = models.CharField(max_length=100)
    fishing_village = models.CharField(max_length=100)
    landing_beach = models.CharField(max_length=100)
    current_canoe_name = models.CharField(max_length=100)
    type_of_ownership = models.CharField(max_length=100)
    name_canoe_owner = models.CharField(max_length=100)
    name_captain = models.CharField(max_length=100)