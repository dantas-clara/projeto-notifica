from django.contrib import admin
from .models import *
from django.contrib import admin
from searchApp.models.Profile import Profile
from searchApp.models import State, City, Neighborhood, Address


class ProfileAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ('user', 'name', 'address', 'civil_status', 'education', 'role', 'birthday')
    list_display_links = ('user', 'role')
    empty_value_display = 'Vazio'
    list_filter = ('user__is_active',)
    exclude = ('favorites', 'created_at', 'updated_at')
    search_fields = ('user__username',)

    fieldsets = (
        ('Dados Pessoais', {
            'fields': ('user', 'name', 'address', 'birthday')
        }),
        ('Dados Socioeconômicos', {
            'fields': ('civil_status', 'education')
        }),
        ('Saúde e Obesidade', {
            'fields': ('health_information',)  # corrigido: singular
        }),
    )

    # Registro dos modelos no admin


admin.site.register(Profile, ProfileAdmin)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Neighborhood)
admin.site.register(Address)
