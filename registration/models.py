from django.db import models

#Registration of canoes
class Manager(models.Model):
    name_of_fisher = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1)
    occupation = models.CharField(max_length=200)
    phone_number = models.IntegerField()
    manager_address = models.CharField(max_length=200)
    number_of_canoes = models.IntegerField(default=0)
    
    hull_material = models.CharField(max_length=200)
    vessel_size = models.DecimalField(max_digits=10, decimal_places=3)
    
    def __unicode(self):
        return self.name_of_fisher
    


class Canoe(models.Model):
    owner = models.ForeignKey(Manager)
    manager_id = models.IntegerField() #Not visible on form
    canoe_id = models.IntegerField() #Not visible on form
    name_of_tech_staff = models.IntegerField() #Not visible on form
    name_of_authority = models.CharField(max_length=40) #Not visible on form
    date_authorized = models.DateField() #Not visible on form
    current_canoe_number = models.IntegerField(default=0)
    coastal_region = models.CharField(max_length=100)
    coastal_district = models.CharField(max_length=100)
    fishing_village = models.CharField(max_length=100)
    landing_beach = models.CharField(max_length=100)
    current_canoe_name = models.CharField(max_length=100)
    type_of_ownership = models.CharField(max_length=100)
    name_canoe_owner = models.CharField(max_length=100)
    name_captain = models.CharField(max_length=100)
    year_purchased = models.IntegerField(default=0)
    year_built = models.IntegerField(default=0)
    place_built = models.IntegerField(default=0)
    first_year_fishing = models.IntegerField(default=0)
    construction_material = models.CharField(max_length=50)
    length_overall = models.IntegerField(default = 0)
    type_storage = models.BooleanField() #True is ice, false is no ice
    crew_number = models.IntegerField()
    is_motorized = models.BooleanField() #True if motorized, false if not
    model_of_engine = models.CharField(max_length=50)
    horsepower = models.IntegerField(default=0)
    first_gear_type = models.CharField(max_length=50)
    second_gear_type = models.CharField(max_length=50)
    third_gear_type = models.CharField(max_length=50)
    equipment_on_board = models.CharField(max_length=50)
    date_of_registration = models.DateField()
    photo_one = models.ImageField(upload_to='static/images') #first photo of canoe
    photo_two = models.ImageField(upload_to='static/images') #second photo of canoe
    has_signature = models.BooleanField() #digital signature of fisherman
    
    