from django.contrib import admin
#from pacientes.models import Paciente
from django.forms import CheckboxSelectMultiple
from pacientes.models import *

class PacienteAdmin(admin.ModelAdmin):
	list_display = ['nome','cpf','telefone','data_nascimento','criado_em']
	search_fields  = ['nome','cpf']
	formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

class UbsAdmin(admin.ModelAdmin):
	list_display = ['nome']
	search_fields  = ['nome']
admin.site.register(Paciente,PacienteAdmin)
admin.site.register(Ubs,UbsAdmin)