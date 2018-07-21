from django.db import models

# Create your models here.
class User(models.Model):
    First_Name=models.CharField(max_length=50)
    Last_Name=models.CharField(max_length=50)
    Email=models.EmailField(max_length=100,unique=True)

    def __str__(self):
        return str(self.First_Name)