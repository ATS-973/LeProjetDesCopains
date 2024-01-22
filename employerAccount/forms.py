from .models import CustomEmployerUser
from django import forms

class CustomEmployerCreationForm(forms.ModelForm):
    class Meta:
        model = CustomEmployerUser
        fields = ('nb_siret',)