from django.contrib import admin
from .models import Abonado

@admin.register(Abonado)
class AbonadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'localidad', 'telefono', 'fecha_ingreso')
    search_fields = ('nombre', 'localidad', 'telefono')