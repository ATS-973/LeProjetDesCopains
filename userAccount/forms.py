from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['profile_picture', 'name', 'first_name', 'actualActivity', 'email', 'phone_number', 'cv', 'genPres', 'threeGoodPoints', 'threeExperiences', 'availability']
        labels = {'profile_picture':'Une photo de vous', 
                  'name':'Nom', 
                  'first_name':'Prénom', 
                  'actualActivity':'A préciser', 
                  'email':'Email utilisé la connexion au compte',
                  'phone_number':'Numéro de téléphone', 
                  'cv':'Lien vers votre CV',
                  'genPres':'Présentation générale',
                  'threeGoodPoints':'Trois qualités qui vous définissent',
                  'threeExperiences':'Maximum trois expériences professionelles'}
        required = {'cv': False if ('genPres' and 'threeGoodPoints' and 'threeExperiences') == None else True}