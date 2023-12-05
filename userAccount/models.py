from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    user_id = models.AutoField(primary_key=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/')
    name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    actualActivity = models.CharField(max_length=500)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    adress = models.TextField(max_length=250)
    cv = models.URLField(null=True)
    genPres = models.TextField(null=True, max_length=1000)
    threeGoodPoints = models.TextField(null=True)
    availability = models.ArrayField(models.CharField(max_length=100)) #A modifier pour choix multiple
    threeExperiences = models.TextField(null=True)
    phone_number = models.CharField(max_length=20)
    #Ajouter le tableau des horaires