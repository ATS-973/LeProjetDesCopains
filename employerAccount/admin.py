from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomEmployerUser
from .managers import CustomEmployerManager
from .forms import CustomEmployerCreationForm

class CustomEmployerAdmin(UserAdmin):
    add_form = CustomEmployerCreationForm
    add_fieldsets = (
        (None, {
            'classes': ('wide'),
            'fields': ('nb_siret','password'),
        }),
    )
    model = CustomEmployerUser

    ordering = ['nb_siret']

    list_display = ['nb_siret']
    search_fields = ['nb_siret']

    fieldsets = (
        (None, {'fields': ('nb_siret', 'password')}),
        ('Infos', {'fields': ('nom_enseigne',)}),
        ('Adresse', {'fields': ('libelle_de_voie', 'code_postal', 'ville')}),
    )

admin.site.register(CustomEmployerUser, CustomEmployerAdmin)