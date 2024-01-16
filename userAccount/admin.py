from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .managers import CustomUserManager
from django import forms


class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('email','first_name', 'last_name', 'profile_picture', 'actualActivity', 'date_of_birth', 'adress', 'cv', 'genPres', 'threeGoodPoints', 'threeExperiences', 'phone_number', 'is_staff', 'is_superuser')

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    add_fieldsets = (
        (None, {
            'classes': ('wide'),
            'fields': ('email', 'password', 'is_active', 'date_joined'),
        }),
    )
    model = CustomUser
    #add_form = CustomUserManager  #A modifier avec un form custom, responsable de l'erreur Add dans url/admin

    ordering = ['email']
    list_filter = ['is_staff', 'is_superuser']

    # Spécifiez les champs qui doivent être affichés dans l'interface d'administration
    list_display = ['email', 'first_name', 'last_name', 'is_staff', 'is_superuser']
    search_fields = ['email', 'first_name', 'last_name']

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'profile_picture', 'actualActivity', 'date_of_birth', 'adress', 'cv', 'genPres', 'threeGoodPoints', 'threeExperiences', 'phone_number')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

# Enregistrez le modèle CustomUser avec l'admin
admin.site.register(CustomUser, CustomUserAdmin)