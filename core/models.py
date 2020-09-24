from django.db import models
from pacientes.utils import SEXO
from controle_usuarios.models import Profissional


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
    nome              = models.CharField('Nome',max_length=60)
    data_nascimento   = models.DateField(blank=True,null=True)
    sexo              = models.CharField('Sexo', max_length=1, choices=SEXO, blank=True)
    cpf               = models.CharField(max_length=14,blank=True,null=True)
    sus               = models.CharField(max_length=18,unique=True,blank=True,null=True)
    #endereco
    telefone          = models.CharField('Telefone Principal',max_length=20)
    telefone_fixo     = models.CharField('Telefone Fixo',max_length=20,blank=True)
    #complemento
    #profissional      = models.ForeignKey(Profissional ,on_delete=models.SET_NULL,null=True)
    profissional      = models.ManyToManyField(Profissional)
    #convenios
    observacao        = models.TextField(max_length=500,blank=True)
    atualizado_em     = models.DateTimeField('Atualizado em', auto_now=True)
    criado_em         = models.DateTimeField('Criado em', auto_now_add=True)

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