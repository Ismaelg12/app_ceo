from django.contrib import admin
from core.models import ListaEspera,Clinica, Novidade


class ListaEsperaAdmin(admin.ModelAdmin):
	list_display 	= ['nome','especialidade','telefone','urgente','criado_em','atualizado_em'] 
	list_filter   	= ['nome','especialidade','urgente']
	search_fields 	= ['especialidade']

class NovidadeAdmin(admin.ModelAdmin):
	list_display 	= ['id','versao','descricao','criado_em','atualizado_em'] 
	list_display_links = ('id','versao')
	
admin.site.register(Clinica)
admin.site.register(Novidade,NovidadeAdmin)
admin.site.register(ListaEspera,ListaEsperaAdmin)

