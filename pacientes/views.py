# -*- coding: utf-8 -*-
from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
from django.urls import reverse_lazy
from pacientes.models import Paciente
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


class PacienteListView(LoginRequiredMixin,ListView):
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


    def get_context_data(self, *args, **kwargs):
        context = super(PacienteListView, self).get_context_data(*args, **kwargs)
        context['profissional_logado'] = Profissional.objects.filter(
            user=self.request.user,tipo=2
        )
        context['paciente_clinico'] = Paciente.objects.prefetch_related('profissional').filter(
            profissional__user=self.request.user)
        #if tiver busca ele filtra os meus pacientes
        if self.request.GET.get('paciente'):
            paciente_search = self.request.GET.get('paciente')
            context['paciente_clinico'] = Paciente.objects.prefetch_related('profissional').filter(
                nome__icontains=paciente_search,profissional__user=self.request.user).order_by('id')
        return context

        
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


class PacienteDetailView(LoginRequiredMixin,DetailView):
    model = Paciente
    template_name = 'paciente_detalhe.html'
    context_object_name = 'paciente'
