from django.db import models

# Create your models here.

class user(models.Model):
    User_name = models.CharField(max_length=30)
    User_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "user31"
