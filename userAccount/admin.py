from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .managers import CustomUserManager
from .forms import CustomUserCreationForm

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
        ('Personal info', {'fields': ('first_name', 'last_name', 'profile_picture', 'actual_activity', 'date_of_birth', 'adress', 'cv', 'general_presentation', 'three_good_points', 'three_experiences', 'phone_number')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

# Enregistrez le modèle CustomUser avec l'admin
admin.site.register(CustomUser, CustomUserAdmin)