from operator import truediv
from pickle import TRUE
from django.db import models


# Create your models here.
class Us(models.Model):
    User_name = models.CharField(max_length=30)
    User_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "us1"
class Demo(models.Model):
    name = models.CharField(max_length=20)


  
