from django.db import models
import datetime
from django.utils import timezone
from pacientes.models import Paciente, Ubs
from controle_usuarios.models import Profissional,Especialidade
from core.utils import STATUS


class Procedimento(models.Model):
    descricao    = models.CharField(max_length=100,blank=True,unique=True)

    class Meta:
        verbose_name = 'Procedimento'
        verbose_name_plural = 'Procedimentos'
        
    def __str__(self):
        return self.descricao

class Odontograma(models.Model):
    descricao    = models.CharField(max_length=100,blank=True,unique=True)

    class Meta:
        verbose_name = 'Odontograma'
        verbose_name_plural = 'Odontogramas'
        
    def __str__(self):
        return self.descricao

class TipoConsulta(models.Model):
    descricao    = models.CharField(max_length=100,blank=True,unique=True)

    class Meta:
        verbose_name = 'TipoConculta'
        verbose_name_plural = 'TipoConculta'
        
    def __str__(self):
        return self.descricao

class Vigilancia(models.Model):
    descricao    = models.CharField(max_length=100,blank=True,unique=True)

    class Meta:
        verbose_name = 'Vigilancia'
        verbose_name_plural = 'Vigilancias'
        
    def __str__(self):
        return self.descricao

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
    procedimento  = models.ManyToManyField(Procedimento)
    odontograma   = models.ManyToManyField(Odontograma)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True) 
    ubs           = models.ForeignKey(Ubs,on_delete=models.PROTECT,null=True,blank=True)
    tipoconsulta  = models.ForeignKey(TipoConsulta,on_delete=models.PROTECT,null=True)
    vigilancia    = models.ManyToManyField(Vigilancia)

    class Meta:
        verbose_name = 'Agendamento'
        verbose_name_plural = 'Agendamentos'
    
    def __str__(self):
        return self.paciente.nome