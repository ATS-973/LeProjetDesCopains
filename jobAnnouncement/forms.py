from .models import Offer
from django import forms

class OfferCreationForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = ('title', 'description', 'horaires', 'employer')