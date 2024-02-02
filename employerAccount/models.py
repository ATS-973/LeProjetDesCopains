from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from .managers import CustomEmployerManager
from api_insee import ApiInsee

api = ApiInsee(
    key = "F16E_kTAmtPLDt1p0bxKTE2UuZ4a",
    secret = "WjR5T2GyB4rojD0nyZxDE1ws65Ia"
)

class CustomEmployerUser(AbstractBaseUser, PermissionsMixin):

    employer_id = models.AutoField(primary_key=True)
    nb_siret = models.CharField(unique=True, max_length=14)
    nom_enseigne = models.CharField(max_length=100, blank=True)
    libelle_de_voie = models.CharField(max_length = 50, blank=True)
    code_postal = models.CharField(max_length=100, blank=True)
    ville = models.CharField(max_length=50, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomEmployerManager()
    
    
    USERNAME_FIELD = 'nb_siret'

    def luhnAlgorythm(self, nb_siret):
        pos = len(nb_siret)-1
        posPar = 1
        somme = 0
        while pos >= 0:
            if posPar%2 != 0:
                somme += int(nb_siret[pos])
            else:
                if len(str(2*int(nb_siret[pos]))) == 2:
                    somme += int(str(2*int(nb_siret[pos]))[0]) + int(str(2*int(nb_siret[pos]))[1])
                else:
                    somme += 2*int(nb_siret[pos])
            pos -= 1
            posPar += 1
            print(somme)
        
        if somme%10 == 0:
            return(True)
        else:
            return(False)
    
    def initialisation(self, nb_siret):
        data = api.siret(str(nb_siret)).get()

        self.nom_enseigne = data["etablissement"]['periodesEtablissement'][0]['enseigne1Etablissement']
        self.libelle_de_voie = data["etablissement"]["adresseEtablissement"]['numeroVoieEtablissement'] + " " + data["etablissement"]["adresseEtablissement"]['typeVoieEtablissement'] + " " + data["etablissement"]["adresseEtablissement"]['libelleVoieEtablissement']
        self.code_postal = data["etablissement"]["adresseEtablissement"]['codePostalEtablissement']
        self.ville = data["etablissement"]["adresseEtablissement"]['libelleCommuneEtablissement']

    def save(self, *args, **kwargs):
        if not self.luhnAlgorythm(self.nb_siret):
            raise ValueError("Le numéro SIRET n'est pas valide")
        else:
            self.initialisation(self.nb_siret)

        super().save(*args, **kwargs)