from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class userdetails(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    
    # additional fields
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    user_img = models.ImageField(upload_to='userimg/',blank=True,null=True)