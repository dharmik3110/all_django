from django.db import models

# Create your models here.


class NewOwner(models.Model):
    owner_name = models.CharField(max_length=30)
    owner_email = models.EmailField(max_length=254)
    owner_address = models.CharField(max_length=50)
    owner_phonenumber = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "newowner"