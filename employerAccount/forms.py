from .models import CustomEmployerUser
from django import forms

class CustomEmployerCreationForm(forms.ModelForm):
    class Meta:
        model = CustomEmployerUser
        fields = ('nb_siret', 'nom_enseigne', 'libelle_de_voie', 'code_postal', 'ville', 'email', 'website', 'phone')

class EmployerLoginForm(forms.ModelForm):
    nb_siret = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        nb_siret= cleaned_data.get('nb_siret')
        password = cleaned_data.get('password')

        if username and password:
            user = CustomEmployerUser.objects.filter(username=username).first()
            if not user or not user.check_password(password):
                raise forms.ValidationError("Numéro siret ou mot de passe incorrect.")

        return cleaned_data