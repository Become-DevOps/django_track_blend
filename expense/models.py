from django.db import models

# Create your models here.
class Expense(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    catogery = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)  
    
    def __str__(self):
        return self.name 