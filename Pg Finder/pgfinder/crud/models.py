from django.db import models
from generic.models import Basefield
# Create your models here.

class  Rooms(Basefield):
    room_availability = models.BooleanField(default=True) 
    room_type = models.CharField(max_length=30, null=True)
    room_sharing = models.CharField(max_length=30)

    class Meta():
        db_table = "roomcat"
    
    def __str__(self):
        return self.room_type

class State(Basefield):
    state_name = models.CharField(max_length=30)
    state_code = models.CharField(max_length=30)
    class Meta():
        db_table="State"


class City(Basefield):
	city_name = models.CharField(max_length=30)
	city_code = models.CharField(max_length=30)
	class Meta():
         db_table = "city"

class Address(Basefield):
    address = models.CharField( max_length=50)
    state = models.ForeignKey(State,on_delete=models.CASCADE)
    city = models.ForeignKey(City,on_delete=models.CASCADE)
    class Meta():
            db_table = "address1"

    def __str__(self):
        return self.address
    

class Pg(Basefield):
    pg_name = models.CharField(max_length=30)
    pg_address = models.ForeignKey(Address,on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=12,null=True)
    
    #pg_availability = models.ForeignKey(Rooms,on_delete=models.CASCADE)
    pg_rooms = models.ForeignKey(Rooms,on_delete=models.CASCADE)
    class Meta():
            db_table = "pg"
