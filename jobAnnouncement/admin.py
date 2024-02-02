from django.contrib import admin
from .models import Offer
from .forms import OfferCreationForm

class OfferAdmin(admin.ModelAdmin):
    add_form = OfferCreationForm
    add_fieldsets = (
        (None, {
            'classes': ('wide'),
            'fields': ('title', 'description', 'horaires', 'employer'),
        })
    )

    model = Offer

    ordering = ['employer']

    list_display = ['employer', 'title']


admin.site.register(Offer, OfferAdmin)