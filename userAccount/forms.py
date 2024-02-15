from .models import CustomUser
from django import forms

class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('email','first_name', 'last_name', 'profile_picture', 'actual_activity', 'date_of_birth', 'adress', 'cv', 'general_presentation', 'three_good_points', 'three_experiences', 'phone_number', 'is_staff', 'is_superuser')

class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            user = CustomUserPersonal.objects.filter(email=email).first()
            if not email or not user.check_password(password):
                raise forms.ValidationError("Email ou mot de passe incorrect.")

        return cleaned_data