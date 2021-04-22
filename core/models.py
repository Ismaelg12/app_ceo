from django.db import models
from pacientes.utils import SEXO, TRATAMENTO, URGENTE
from controle_usuarios.models import Profissional
from pacientes.models import Paciente
from django.utils import timezone
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

class Especialidade(models.Model):
    #informações basicas
    nome              = models.CharField(max_length=100, blank=False)
    atualizado_em     = models.DateTimeField('Atualizado em', auto_now=True)
    criado_em         = models.DateTimeField('Criado em', auto_now_add=True)


    class Meta:
        verbose_name = 'Especialidade'
        verbose_name_plural = 'Especialidades'

    def __str__(self):
        return self.nome
        
class ListaEspera(models.Model):
    #informações basicas
    nome              = models.ForeignKey(Paciente,on_delete=models.PROTECT,null=True,blank=False)
    profissional      = models.ForeignKey(Profissional,on_delete=models.PROTECT,null=True,blank=False)
    especialidade     = models.ForeignKey(Especialidade,on_delete=models.PROTECT,null=True,blank=False)
    observacao        = models.TextField(max_length=500,blank=True)
    atualizado_em     = models.DateTimeField('Atualizado em', auto_now=True)
    criado_em         = models.DateTimeField(blank=True,null=True)
    urgente           = models.CharField('Urgente', max_length=1, choices=URGENTE, blank=True)

    def get_idade(self):
        return int(datetime.now().date() - datetime.now().date())

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