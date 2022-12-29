from django.db import models

#models.py
class Employee(models.Model):  
    name = models.CharField(max_length=100)  
    email = models.EmailField()  
    contact = models.CharField(max_length=15) 
  
    class Meta:  
        db_table = "employee"


class Photo(models.Model):
    files = models.FileField()
    instructions = models.CharField(max_length=255, blank=True)
