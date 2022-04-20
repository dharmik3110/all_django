from unicodedata import name
from django.db import models

# Create your models here.
from generic.models import Basefield

class NewClass(Basefield):
    new_name = models.CharField(max_length=30)
    new_email = models.EmailField(max_length=254)
    new_address = models.CharField(max_length=50)
    new_phonenumber = models.CharField(max_length=10)

    def __str__(self):
        return self.new_name

        