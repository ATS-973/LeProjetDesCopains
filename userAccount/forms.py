from .models import CustomUser
from django import forms

class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('email','first_name', 'last_name', 'profile_picture', 'actual_activity', 'date_of_birth', 'adress', 'cv', 'general_presentation', 'three_good_points', 'three_experiences', 'phone_number', 'is_staff', 'is_superuser')
