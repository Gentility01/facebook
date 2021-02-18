from django.db import models
from django.contrib.auth.models import User

# Create your models here.


#login model
class Form(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name='+')
    phone = models.IntegerField()
    password = models.CharField(max_length=50)
    slug = models.SlugField()
    GENDER_MALE = 0
    GENDER_FEMALE = 1
    GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female')]
    gender = models.IntegerField(choices=GENDER_CHOICES)
  


    