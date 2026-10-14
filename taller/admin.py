from django.contrib import admin
from .models import Cliente, Reparacion


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'rut', 'telefono', 'email')
    list_filter = ('nombre',)
    search_fields = ('nombre', 'rut', 'email')


@admin.register(Reparacion)
class ReparacionAdmin(admin.ModelAdmin):
    list_display = ('descripcion', 'cliente', 'costo', 'fecha', 'terminada')
    list_filter = ('terminada', 'fecha')
    search_fields = ('descripcion', 'cliente__nombre')