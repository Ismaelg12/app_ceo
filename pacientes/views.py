# -*- coding: utf-8 -*-
from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
from django.urls import reverse_lazy
from pacientes.models import Paciente
from agenda.models import Agendamento
from core.mixins import DashboardMixin
from controle_usuarios.models import Profissional
from django.contrib import messages
from pacientes.forms import PacienteForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.db.models import ProtectedError
from django.http import HttpResponseRedirect
from django.urls import reverse
'''
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+                          Crud de Pacientes/Clientes
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''

class PacienteCreateView(LoginRequiredMixin,CreateView):
    model         = Paciente
    template_name = 'adicionar_paciente.html'
    form_class    = PacienteForm
    success_url   = reverse_lazy('lista_pacientes')
    #salvar e adicionar novo 
    def post(self, request, *args, **kwargs):
        save_action = None
        if "cancelar" in request.POST:
            return HttpResponseRedirect(reverse('lista_pacientes'))
        else:
            save_action = super(PacienteCreateView, self).post(request, *args, **kwargs)
        if "adicionar_outro" in request.POST:
            messages.success(request,'Paciente Cadastrado com Sucesso! ')
            return HttpResponseRedirect(reverse('add_paciente'))
        return save_action


class PacienteListView(LoginRequiredMixin,ListView,DashboardMixin):
    model               = Paciente
    template_name       = 'pacientes.html'
    context_object_name = 'pacientes'
    paginate_by = 50

    def get_queryset(self, **kwargs):
        queryset = Paciente.objects.prefetch_related('profissional').all()
        if self.request.GET.get('paciente'):
            paciente_search = self.request.GET.get('paciente')
            queryset = Paciente.objects.filter(
                nome__icontains=paciente_search).prefetch_related('profissional').order_by('id')
        return queryset

class IniciadoListView(LoginRequiredMixin,ListView,DashboardMixin):
    model               = Paciente
    template_name       = 'trat_iniciado.html'
    context_object_name = 'pacientes'
    paginate_by = 50
    def get_queryset(self, **kwargs):
        queryset = Paciente.objects.prefetch_related('profissional').all()
        if self.request.GET.get('paciente'):
            paciente_search = self.request.GET.get('paciente')
            queryset = Paciente.objects.filter(
                nome__icontains=paciente_search).prefetch_related('profissional').order_by('id')
        return queryset

class ConcluidoListView(LoginRequiredMixin,ListView,DashboardMixin):
    model               = Paciente
    template_name       = 'trat_concluido.html'
    context_object_name = 'pacientes'
    paginate_by = 50
    def get_queryset(self, **kwargs):
        queryset = Paciente.objects.prefetch_related('profissional').all()
        if self.request.GET.get('paciente'):
            paciente_search = self.request.GET.get('paciente')
            queryset = Paciente.objects.filter(
                nome__icontains=paciente_search).prefetch_related('profissional').order_by('id')
        return queryset

class LigacaoListView(LoginRequiredMixin,ListView,DashboardMixin):
    model               = Paciente
    template_name       = 'ligacao.html'
    context_object_name = 'pacientes'
    paginate_by = 50
    def get_queryset(self, **kwargs):
        queryset = Paciente.objects.prefetch_related('profissional').all()
        if self.request.GET.get('paciente'):
            paciente_search = self.request.GET.get('paciente')
            queryset = Paciente.objects.filter(
                nome__icontains=paciente_search).prefetch_related('profissional').order_by('id')
        return queryset

class PacienteUpdateView(LoginRequiredMixin,UpdateView):
    model = Paciente
    template_name = 'adicionar_paciente.html'
    form_class    = PacienteForm
    success_url   = reverse_lazy('lista_pacientes')


@login_required 
def PacienteDeleteView(request,pk):
    try :
        paciente = get_object_or_404(Paciente, pk=pk).delete()
        messages.error(request,'Paciente Deletado Com Sucesso.')
    except ProtectedError:
        messages.warning(request,
         "você não pode deletar esse paciente porque ele tem atendimentos ou agendamentos feitos")
    return redirect('lista_pacientes')


# class PacienteDetailView(LoginRequiredMixin,DetailView):
#     model = Paciente
#     template_name = 'paciente_detalhe.html'
#     context_object_name = 'paciente'

@login_required
def PacienteDetailView(request,pk):
    agendamento      = get_object_or_404(Agendamento,pk=pk)
    paciente = Paciente.objects.get(pk=pk)
    profissional = ""
    agenda = Agendamento.objects.filter(paciente=paciente)
    context = {
        'paciente':paciente,
        'agenda':agenda,
    }
    print(context,"Agenda de pacientes cadastrados no sistema")
    return render(request,'paciente_detalhe.html',context)

@login_required 
def paciente_historico(request,pk):
    profissional = ""
    atendente    = Profissional.prof_objects.filter(user=request.user,tipo=1)
    paciente              = get_object_or_404(Paciente,pk=pk)
    agenda_obs= Agendamento.objects.filter(paciente=paciente)
    ######################################################

    #quesyset apenas para condição no template
    if atendente.exists() or request.user.is_superuser:
        #não faz nada :)
        pass
    else:
        profissional = Profissional.prof_objects.get(user=request.user,tipo=2)

    #lista todos os atendimentos na 1ª aba e 2ª aba linha do tempo
    if profissional:
        atendimentos    = Agendamento.objects.filter(paciente=paciente,profissional_id=profissional.id)
    else:
        atendimentos      = Agendamento.objects.filter(paciente=paciente)

    agendamentos_count    = Agendamento.objects.filter(paciente=paciente).count()
    agendamentos_AG_count = Agendamento.objects.filter(paciente=paciente,status='AG').count()
    agendamentos_AT_count = Agendamento.objects.filter(paciente=paciente,status='AT').count()
    agendamentos_FN_count = Agendamento.objects.filter(paciente=paciente,status='FN').count()
    agendamentos_DM_count = Agendamento.objects.filter(paciente=paciente,status='DM').count()


    context = {
        'profissional':profissional,
        'paciente':paciente,
        'agendamentos':agendamentos_count,
        'agendamentos_AG_count':agendamentos_AG_count,
        'agendamentos_AT_count':agendamentos_AT_count,
        'agendamentos_FN_count':agendamentos_FN_count,
        'agendamentos_DM_count':agendamentos_DM_count,
        'linha_do_tempo':atendimentos,
        'agenda_obs':agenda_obs,
    }
    return render(request,'historico.html',context)