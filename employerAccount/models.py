from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from .managers import CustomEmployerManager
import api_insee

class CustomEmployerUser(AbstractBaseUser, PermissionsMixin):
    employer_id = models.AutoField(primary_key=True)
    nb_siret = models.CharField(unique=True, max_length=14)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomEmployerManager()
    
    USERNAME_FIELD = 'nb_siret'

    def luhnAlgorythm(self, nb_siret):
        pos = len(nb_siret)-1
        posPar = 1
        somme = 0
        for i in range(len(nb_siret)-1, 0, -1):
            if posPar%2 == 0:
                somme += 2*int(nb_siret[i])
            else:
                somme += int(nb_siret[i])
        if somme%10 == 0:
            return(True)
        else:
            return(False)

    def save(self, *args, **kwargs):
        if not self.luhnAlgorythm(self.nb_siret):
            raise ValueError("Le numéro SIRET n'est pas valide")

        super().save(*args, **kwargs)