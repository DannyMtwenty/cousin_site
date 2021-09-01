from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
# class User(AbstractUser):
#    img= models.ImageField(upload_to='pics')



class Member(models.Model):
    Chairperson = 'Chairperson '
    ViceChairpersion = 'Vice Chairpersion'
    Secretary = 'Secretary'
    Treasurer = 'Treasurer'
    member = 'Member'
    Roles_member = [
        (Chairperson ,'Chairperson '),
        (ViceChairpersion, 'Vice Chairpersion'),
        (Secretary ,'Secretary'),
        (Treasurer, 'Treasurer'),
        (member ,'Member')
    ]
    FirstName=models.CharField(max_length=200)
    LastName = models.CharField(max_length=200)
    role= models.CharField(max_length=200, choices=Roles_member, default=member)
    img= models.ImageField(upload_to='pics')

class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class Photo(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(null=False, blank=False)
    description = models.TextField()

    def __str__(self):
        return self.description