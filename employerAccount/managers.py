from django.contrib.auth.models import BaseUserManager
from api_insee import ApiInsee
import requests

data = {}

api = ApiInsee(
    key = "F16E_kTAmtPLDt1p0bxKTE2UuZ4a",
    secret = "WjR5T2GyB4rojD0nyZxDE1ws65Ia"
)

def check_api_siret(nb_siret):
    try:
        response = api.siret(nb_siret).get()
        
        if response.status_code == 404:
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        print(f"Erreur de requête : {e}")
        return False

class CustomEmployerManager(BaseUserManager):
    def create_user(self, nb_siret, password=None, **extra_fields):
        if check_api_siret(nb_siret):
            raise ValueError("L'API a retourné une erreur 404.")

        user = self.model(nb_siret=nb_siret, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        
        