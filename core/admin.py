from django.contrib import admin
from core.models import ListaEspera,Clinica,Especialidade

class EspecialidadeAdmin(admin.ModelAdmin):
	list_display = ['nome'] 

class ListaEsperaAdmin(admin.ModelAdmin):
	list_display = ['nome','profissional','especialidade'] 
	
admin.site.register(Clinica)
admin.site.register(ListaEspera,ListaEsperaAdmin)
admin.site.register(Especialidade,EspecialidadeAdmin)