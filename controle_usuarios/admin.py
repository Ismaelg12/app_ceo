from django.contrib import admin
from controle_usuarios.models import Profissional,Especialidade


class ProfissionalAdmin(admin.ModelAdmin):
	list_display = ['user','nome','sobrenome','tipo','email', 'ativo','especialidade'] 
	search_fields = ['nome']

class EspecialidadeAdmin(admin.ModelAdmin):
	list_display = ['id','especialidade'] 

admin.site.register(Profissional,ProfissionalAdmin)
admin.site.register(Especialidade,EspecialidadeAdmin)

