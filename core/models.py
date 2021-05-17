from django.db import models
from pacientes.utils import SEXO, TRATAMENTO, URGENTE
from controle_usuarios.models import Profissional,Especialidade
from pacientes.models import Paciente
from datetime import datetime


class TimeStampedModel(models.Model):
    created = models.DateTimeField(
        'criado em',
        auto_now_add=True,
        auto_now=False
    )
    modified = models.DateTimeField(
        'modificado em',
        auto_now_add=False,
        auto_now=True
    )

    class Meta:
        abstract = True

        
class ListaEspera(models.Model):
    #informações basicas
    nome              = models.ForeignKey(Paciente,on_delete=models.PROTECT,null=True,blank=False)
    telefone          = models.CharField(max_length=16,blank=True)
    especialidade     = models.ForeignKey(Especialidade,on_delete=models.PROTECT,null=True,blank=False)
    observacao        = models.TextField(max_length=500,blank=True)
    atualizado_em     = models.DateTimeField('Atualizado em', auto_now=True)
    criado_em         = models.DateField(blank=True,null=True)
    urgente           = models.CharField('Urgente', max_length=1, choices=URGENTE, blank=True)

    def espera(self):
        return int((datetime.now().date()-self.criado_em).days)

    class Meta:
        verbose_name = 'Lista de Espera'
        verbose_name_plural = 'Listas de Espera'

    def __str__(self):
        return self.nome


class Clinica(models.Model):
    logo_menu   = models.ImageField(upload_to='media')
    clinica     = models.CharField(max_length=50,blank=True)
    sobre_nos   = models.TextField(max_length=600,blank=True)

    class Meta:
        verbose_name = 'Clinica '
        verbose_name_plural = 'Clinica'
        
    def __str__(self):
        return self.clinica