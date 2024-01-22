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
    )

admin.site.register(CustomEmployerUser, CustomEmployerAdmin)