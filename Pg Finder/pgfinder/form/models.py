from django.db import models
from django.forms import CharField

# Create your models here.

class Address(models.Model):
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    
    class Meta():
        db_table = "address"


