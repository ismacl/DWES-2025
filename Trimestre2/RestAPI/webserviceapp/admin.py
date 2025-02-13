from django.contrib import admin
from .models import *


# Register your models here.

class usuariosExistentes(admin.ModelAdmin):
    list_display = ('first_name', 'tipo')
    search_fields = ('tipo',)


class eventosExistentes(admin.ModelAdmin):
    list_display = ('titulo', 'descripcion', 'organizador', 'capacidad_maxima')
    search_fields = ('titulo',)

class comentariosExistentes(admin.ModelAdmin):
    list_display = ('usuario', 'fecha_publicacion', 'evento', 'comentario')
    search_fields = ('',)

class reservasExistentes (admin.ModelAdmin):
    list_display = ('evento', 'usuario', 'entradas')
    search_fields = ('tipo',)

admin.site.register(Tusuarios, usuariosExistentes)
admin.site.register(Teventos, eventosExistentes)
admin.site.register(Tcomentarios, comentariosExistentes)
admin.site.register(Treservas, reservasExistentes)


