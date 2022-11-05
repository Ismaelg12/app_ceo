from django.contrib import admin
from core.models import ListaEspera,Clinica


class ListaEsperaAdmin(admin.ModelAdmin):
	list_display 	= ['nome','especialidade','telefone','urgente','criado_em','atualizado_em'] 
	list_filter   	= ['nome','especialidade','urgente']
	search_fields 	= ['especialidade']
	
admin.site.register(Clinica)
admin.site.register(ListaEspera,ListaEsperaAdmin)
