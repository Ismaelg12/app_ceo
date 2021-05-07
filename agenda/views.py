# -*- coding: utf-8 -*-
from django.utils import timezone
from agenda.forms import AgendaForm
import json
from django.urls import reverse_lazy
from datetime import date, datetime, timedelta
from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView,CreateView,TemplateView,UpdateView,DeleteView,DetailView
from django.http import JsonResponse
from django.template.loader import render_to_string
from agenda.models import Agendamento
from pacientes.models import Paciente
from core.models import ListaEspera
from controle_usuarios.models import Profissional
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import ProtectedError
from django.forms import inlineformset_factory
from dateutil.relativedelta import relativedelta
from django.contrib.auth.mixins import LoginRequiredMixin
from core.decorators import staff_member_required

# @method_decorator(staff_member_required, name='dispatch')
class AgendaCreateView(LoginRequiredMixin,CreateView):
    model         = Agendamento
    template_name = 'agendas/agenda_add.html'
    form_class    = AgendaForm
    success_url   = reverse_lazy('agendas')

    #salvar e adicionar novo
    def post(self, request, *args, **kwargs):
        save_action = None
        if "cancelar" in request.POST:
            return HttpResponseRedirect(reverse('agendas'))
        else:
            save_action = super(AgendaCreateView, self).post(request, *args, **kwargs)
            agen = ListaEspera.objects.filter(nome__id=request.POST['paciente'],
                especialidade_id=request.POST['especialidade']).delete()
        if "adicionar_outro" in request.POST:
            messages.success(request,'Agendamento Cadastrado com Sucesso! ')
            return HttpResponseRedirect(reverse('add_agenda'))    
        return save_action


@login_required
def agendamento(request):
    #armazena os dados de atuação do profisional logado
    lista = []
    #atendente e profissional
    #pf é querysets para exibir profissionais no template para o filtro
    pf                  = Profissional.prof_objects.filter(tipo=2).values('id',
     'nome','sobrenome').exclude(user__username='admin')
    #at querysets para fazer condição no template e determinar o que deve ser exibido
    at                  = Profissional.prof_objects.filter(user=request.user,tipo=1)
    profissional        = Profissional.prof_objects.filter(user=request.user,tipo=2)

    if profissional.exists():
        pff = Profissional.objects.get(user=request.user,tipo=2)      
        # for i in pff.especialidade.all():
        #     lista.append(i.get_id_display())
    else:
        pass
            #print (i)
    date_range          = None
    start_date_string   = None
    end_date_string     = None
    agendamentos        = None
    agenda_profissional = None
    #verifica quem esta logado, se for profissional retorna True e mostra apenas os agendamentos dele liberados
    if profissional.exists():
        if request.GET.get('date_ranger'):
            date_range        = request.GET.get('date_ranger')
            start_date_string = datetime.strptime(date_range.split(' / ')[0],'%d/%m/%Y').strftime('%Y-%m-%d')
            end_date_string   = datetime.strptime(date_range.split(' / ')[1],'%d/%m/%Y').strftime('%Y-%m-%d')
            status            = request.GET.get('status')
            paciente          = request.GET.get('paciente')
            if status != None:
                agenda_profissional = Agendamento.objects.select_related('paciente',
            'profissional').filter(data__range=(start_date_string,end_date_string),
                status=status,paciente__nome__icontains=paciente,profissional__user=request.user)
            else:
                agenda_profissional = Agendamento.objects.select_related('paciente',
            'profissional').filter(data__range=(start_date_string,end_date_string),
                paciente__nome__icontains=paciente,profissional__user=request.user)
        else:
            today = timezone.now()
            agenda_profissional = Agendamento.objects.select_related('paciente',
            'profissional').filter(profissional__user=request.user,
                    data__day=today.day,data__month=today.month)
    else:
        #se for False retorna todos os agendamentos independente de admin ou atendente
        if request.GET.get('date_ranger'):
            date_range          = request.GET.get('date_ranger')
            start_date_string   = datetime.strptime(date_range.split(' / ')[0],'%d/%m/%Y').strftime('%Y-%m-%d')
            end_date_string     = datetime.strptime(date_range.split(' / ')[1],'%d/%m/%Y').strftime('%Y-%m-%d')
            profissional_search = request.GET.get('profissional')
            status              = request.GET.get('status')
            paciente            = request.GET.get('paciente')
            if status != None:
                agendamentos = Agendamento.objects.select_related('paciente',
'profissional').filter(data__range=(start_date_string,end_date_string),
                profissional__nome__icontains=profissional_search,status=status,paciente__nome__icontains=paciente)
            else:
                agendamentos = Agendamento.objects.select_related('paciente',
'profissional').filter(data__range=(start_date_string,end_date_string),
                profissional__nome__icontains=profissional_search,paciente__nome__icontains=paciente)
        else:
            today = timezone.now()
            agendamentos = Agendamento.objects.select_related('paciente',
'profissional').filter(data__day=today.day,
                data__month=today.month)
     
    context = {
        'pf':pf,
        'at':at,
        'profissional':profissional,
        'agendamentos':agendamentos,
        'af':agenda_profissional,
        'lista_fichas_options':lista,

    }
    return render(request,'agendas/agendas.html',context)

# @method_decorator(staff_member_required, name='dispatch')
class AgendaUpdateView(LoginRequiredMixin,UpdateView):
    model         = Agendamento
    template_name = 'agendas/agenda_add.html'
    form_class    = AgendaForm
    success_url   = reverse_lazy('agendas')

class AgendaStatusView(LoginRequiredMixin,UpdateView):
    model         = Agendamento
    template_name = 'agendas/agenda_status.html'
    form_class    = AgendaForm
    success_url   = reverse_lazy('agendas')

# @method_decorator(staff_member_required, name='dispatch')
class AgendaDeleteView(LoginRequiredMixin,DeleteView):
    model         = Agendamento
    success_url   = reverse_lazy('agendas')
    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

@login_required
def Agenda_detalhe(request,pk):
    agenda = Agendamento.objects.get(pk=pk)
    context = {
        'agenda':agenda,
    }
    return render(request,'agendas/agenda_detalhe.html',context)