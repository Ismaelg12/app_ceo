from django.contrib import admin
from agenda.models import Agendamento
# Register your models here.

class AgendamentoAdmin(admin.ModelAdmin):
	list_display  = ['data','paciente','profissional',
		'status', 'hora']
	list_filter   = ['data','profissional','status']
	search_fields = ['data','paciente__nome']

admin.site.register(Agendamento, AgendamentoAdmin)