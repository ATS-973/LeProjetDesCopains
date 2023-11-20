from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    actualActivity = models.CharField(max_length=500)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    profile_picture = models.ImageField(upload_to='profile_pics/') #A modifier pour pointer vers le dossier
    adress = models.TextField()
    cv = models.CharField(max_length=1000)
    genPres = models.TextField()
    threeGoodPoints = models.TextField()
    availability = models.ArrayField(models.CharField(max_length=100))
    experience = models.TextField()