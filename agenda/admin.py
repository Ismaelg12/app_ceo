from django.contrib import admin
from agenda.models import Agendamento, Procedimento, Odontograma, TipoConsulta, Vigilancia
# Register your models here.


class OdontogramaAdmin(admin.ModelAdmin):
	list_display  = ['descricao']

class ProcedimentoAdmin(admin.ModelAdmin):
	list_display  = ['descricao']

class TipoConsultaAdmin(admin.ModelAdmin):
	list_display  = ['descricao']

class VigilanciaAdmin(admin.ModelAdmin):
	list_display  = ['descricao']

class AgendamentoAdmin(admin.ModelAdmin):
	list_display  = ['data','paciente','profissional',
		'status','ubs','observacao']
	list_filter   = ['data','profissional','status']
	search_fields = ['data','paciente__nome']

admin.site.register(Agendamento, AgendamentoAdmin)
admin.site.register(Procedimento, ProcedimentoAdmin)
admin.site.register(Odontograma, OdontogramaAdmin)
admin.site.register(TipoConsulta, TipoConsultaAdmin)
admin.site.register(Vigilancia, VigilanciaAdmin)