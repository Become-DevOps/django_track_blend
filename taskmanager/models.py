from django.db import models

# Create your models here.
class Tasks(models.Model):
    taskid = models.CharField(max_length=100)
    taskname = models.CharField(max_length=100)
    assigned_by = models.CharField(max_length=100)
    assigned_to = models.CharField(max_length=100)
    review = models.CharField(max_length=100)
    priority = models.CharField(max_length=100)