from django.db import models

# Create your models here.

class Form(models.Model):

    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=80)
    position = models.CharField(max_length=80)
    experience = models.CharField(max_length=50)
    available = models.DateField()
    terms = models.BooleanField(default=False)
    newsletter = models.BooleanField(default=False)

    def __str__(self):
         
         return f"{self.first_name} {self.last_name}"
