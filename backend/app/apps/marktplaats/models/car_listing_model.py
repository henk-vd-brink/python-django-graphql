from django.db import models

class CarListingModel(models.Model):
    id = models.IntegerField(primary_key=True, null=False)
    title = models.CharField(max_length=50)
    price = models.IntegerField(blank=True, null=True)
    brand_model = models.CharField(max_length=50)
    mileage = models.IntegerField(blank=True, null=True)
    fuel_type = models.CharField(max_length=50)
    year_of_construction = models.IntegerField(blank=True, null=True)
    category = models.CharField(max_length=50)
    apk_till = models.CharField(max_length=50)
    wheel_base = models.CharField(max_length=50)
    engine_capacity = models.CharField(max_length=50)
    
    class Meta:
        managed = True
        db_table = "CarListings"
    
