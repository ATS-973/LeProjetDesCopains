from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from .managers import CustomEmployerManager
import api_insee

class CustomEmployerUser(AbstractBaseUser, PermissionsMixin):
    employer_id = models.AutoField(primary_key=True)
    nb_siret = models.CharField(unique=True, max_length=20)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomEmployerManager()
    
    USERNAME_FIELD = 'nb_siret'