# -*- coding: utf-8 -*-
from django.db import models
from .utils import SEXO, TRATAMENTO
from core.models import *
from controle_usuarios.models import Profissional
from django.urls import reverse 
from datetime import datetime
import os
from binascii import hexlify


class Ubs(models.Model):
	nome   	= models.CharField(max_length=100,blank=True,unique=True)

	class Meta:
		verbose_name = 'Ubs'
		verbose_name_plural = 'Ubs'
		
	def __str__(self):
		return self.nome

class Paciente(models.Model):
	#informações basicas do paciente
	def generate_id():
		possible = hexlify(os.urandom(4))
		try:
			Paciente.objects.get(id=possible)
		except Paciente.DoesNotExist:
			return possible
		else:
			return self.generate_id()
	id = models.CharField(max_length=8, primary_key=True, editable=False, default=generate_id)
	nome              	= models.CharField('Nome',max_length=60)
	data_nascimento   	= models.DateField(blank=True,null=True)
	sexo              	= models.CharField('Sexo', max_length=1, choices=SEXO, blank=True)
	cpf               	= models.CharField(max_length=14,unique=True,blank=True,null=True)
	sus               	= models.CharField(max_length=18,unique=True,blank=True,null=True)
	#endereco
	cidade      		= models.CharField(max_length=100,blank=True)
	rua   				= models.CharField(max_length=100,blank=True)
	numero   			= models.CharField(max_length=6,blank=True)
	bairro      		= models.CharField(max_length=100,blank=True)
	telefone         	= models.CharField('Celular',max_length=15)
	ubs		      	  	= models.ForeignKey(Ubs,on_delete=models.PROTECT,null=True,blank=True)
	#convenios
	observacao        	= models.TextField(max_length=500,blank=True)
	atualizado_em     	= models.DateTimeField('Atualizado em', auto_now=True)
	criado_em         	= models.DateTimeField('Criado em', auto_now_add=True)
	


	class Meta:
		verbose_name = 'paciente'
		verbose_name_plural = 'pacientes'
		ordering = ['nome']
		
	def __str__(self):
		return self.nome
		
	def idade(self):
		return int((datetime.now().date()-self.data_nascimento).days/365.25)
