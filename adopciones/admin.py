from django.contrib import admin
from .models import*

admin.site.register(Mascotas)

@admin.register(Perfiles)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'bio', 'web')
