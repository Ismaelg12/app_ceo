from django.db import models
import datetime
from django.utils import timezone
from pacientes.models import Paciente
from controle_usuarios.models import Profissional,Especialidade
from core.utils import STATUS


class Agendamento(models.Model):
    id            = models.AutoField(primary_key=True)
    data          = models.DateField(null=True)
    hora 		  = models.TimeField(null=True)
    paciente      = models.ForeignKey(Paciente,on_delete=models.PROTECT)
    telefone      = models.CharField(max_length=15,blank=True)
    profissional  = models.ForeignKey(Profissional,on_delete=models.PROTECT, blank=True)
    especialidade = models.ForeignKey(Especialidade,on_delete=models.PROTECT, blank=True)
    observacao    = models.TextField(blank=True)
    criado_em     = models.DateTimeField('Criado em', auto_now_add=True)
    status        = models.CharField(max_length=2,choices=STATUS,default='AG',blank=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True) 
    

    class Meta:
        verbose_name = 'Agendamento'
        verbose_name_plural = 'Agendamentos'
    
    def __str__(self):
        return self.paciente.nome