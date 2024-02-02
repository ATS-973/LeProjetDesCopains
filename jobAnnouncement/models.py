from django.db import models
from employerAccount.models import CustomEmployerUser

class Offer(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1500)
    horaires = models.CharField(max_length=500)
    employer = models.ForeignKey(CustomEmployerUser, on_delete=models.CASCADE)

#Pour mettre en relation avec annonceur : https://docs.djangoproject.com/fr/5.0/topics/db/examples/many_to_one/