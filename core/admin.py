from django.contrib import admin
from core.models import ListaEspera,Clinica


class ListaEsperaAdmin(admin.ModelAdmin):
	list_display = ['nome','especialidade'] 
	
admin.site.register(Clinica)
admin.site.register(ListaEspera,ListaEsperaAdmin)
