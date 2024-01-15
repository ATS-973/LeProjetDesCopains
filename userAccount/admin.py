from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .managers import CustomUserManager

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserManager

    ordering = ['email']
    list_filter = ['is_staff', 'is_superuser']

    # Spécifiez les champs qui doivent être affichés dans l'interface d'administration
    list_display = ['email', 'first_name', 'last_name', 'is_staff', 'is_superuser']
    search_fields = ['email', 'first_name', 'last_name']

# Enregistrez le modèle CustomUser avec l'admin
admin.site.register(CustomUser, CustomUserAdmin)