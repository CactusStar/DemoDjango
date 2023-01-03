from django.db import models

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32) 
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    publish = models.CharField(max_length=32) 
