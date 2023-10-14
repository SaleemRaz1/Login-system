from django.db import models

# Create your models here.
class Registration(models.Model):
    firstName=models.CharField(max_length=100)
    lastName=models.CharField(max_length=100)
    sex=models.CharField(max_length=50)
    email=models.EmailField(null=False,max_length=254)
    password=models.CharField(max_length=90)
    def __str__(self):
        return self.firstName