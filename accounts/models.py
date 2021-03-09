from django.db import models
from django.contrib.auth.models import User
# from PIL import image

# Create your models here.


#login model
class Form(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    phone = models.IntegerField()
    password = models.CharField(max_length=50)
    slug = models.SlugField()
    GENDER_MALE = 0
    GENDER_FEMALE = 1
    GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female')]
    gender = models.IntegerField(choices=GENDER_CHOICES)
    image = models.ImageField(default ='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f"{self.user.username}'s Profile"

    # def save(self):
    #     super().save()   

    # img = Image.open(self.image.path)

    # if img.height >300 or img.width > 300:
    #     output_size =(300,300) 

    #     img.thumbnail(output_size)
    #     img.save(self.image.path)    
    


    



  


    