from django.db import models

# Create your models here.
class Member(models.Model):    
    FirstName=models.CharField(max_length=200)
    LastName = models.CharField(max_length=200)
    role= models.CharField(max_length=200)
    img= models.ImageField(upload_to='pics')