# -*- coding: utf-8 -*-
from django.db.models import Count
import datetime
from pacientes.models import Paciente
from agenda.models import Agendamento
from produto.models import Produto
from core.models import ListaEspera
from django.utils import timezone
from controle_usuarios.models import Profissional

class DashboardMixin(object):
	
	def clientes(self):
		profissional = Profissional.objects.filter(
			user=self.request.user,tipo=2)

		if profissional:
			paciente_count = Paciente.objects.filter(
				profissional=profissional[0]).count()
		else:
			paciente_count = Paciente.objects.all().count()
		return paciente_count
	#def convenios(self):
		#return Convenio.objects.all().count()

	def birthday(self):
		today     = timezone.now().date()
		return Paciente.objects.filter(data_nascimento__day=today.day,
			data_nascimento__month=today.month).count()
	
	def agendamentos(self):
		today = timezone.now().date()
		agenda_count = Agendamento.objects.filter(data__day=today.day,
			data__month=today.month,status='AG').count()
		return agenda_count

	def produtos(self):
		produto_count = Produto.objects.all().count()
		return produto_count

	def list_espera(self):
		list_espera_count = ListaEspera.objects.all().count()
		return list_espera_count

	def iniciado(self):
		iniciado_count = Paciente.objects.filter(tratamento='IN').count()
		return iniciado_count

	def concluido(self):
		concluido_count = Paciente.objects.filter(tratamento='CO').count()
		return concluido_count

	def liga(self):
		liga_count = Paciente.objects.filter(tratamento='RE').count()
		return liga_count