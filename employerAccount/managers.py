from django.contrib.auth.models import BaseUserManager
from api_insee import ApiInsee
import requests

class CustomEmployerManager(BaseUserManager):
    def create_user(self, nb_siret, password=None, **extra_fields):

        user = self.model(nb_siret=nb_siret, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        
        