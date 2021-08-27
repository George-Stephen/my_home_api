from django.db import models
from cloudinary.models import CloudinaryField
from django.db.models.fields import DecimalField, IntegerField

class Apartment(models.Model):
 main_image = CloudinaryField('image')
 title = models.CharField(max_length=255)
 location = models.CharField(max_length=255)
 description = models.CharField(max_length=255)
 bedrooms = IntegerField()
 bathrooms = IntegerField()
 lat = DecimalField(max_digits=15,decimal_places=8)
 long = DecimalField(max_digits=15,decimal_places=8)
 bath_image = CloudinaryField('image')
 bed_image = CloudinaryField('image')
 price  = IntegerField()
 status = models.CharField(max_length=255)

def __str__(self):
        return self.title

# Create your models here.
