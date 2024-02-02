from django.contrib.auth.models import BaseUserManager
from api_insee import ApiInsee
import requests

api = ApiInsee(
    key = "F16E_kTAmtPLDt1p0bxKTE2UuZ4a",
    secret = "WjR5T2GyB4rojD0nyZxDE1ws65Ia"
)

class CustomEmployerManager(BaseUserManager):
    def create_user(self, nb_siret, password=None, **extra_fields):

        user = self.model(nb_siret=nb_siret, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        
        