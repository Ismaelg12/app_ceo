from django.contrib import admin
from core.models import ListaEspera,Clinica


class ListaEsperaAdmin(admin.ModelAdmin):
	list_display = ['nome','especialidade','telefone','urgente'] 
	list_filter   = ('nome','especialidade','urgente')
	search_fields = ('nome', 'especialidade')
	
admin.site.register(Clinica)
admin.site.register(ListaEspera,ListaEsperaAdmin)
