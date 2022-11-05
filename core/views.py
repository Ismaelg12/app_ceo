# -*- coding: utf-8 -*-
from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import ListView,CreateView,TemplateView,UpdateView,DeleteView,DetailView
from django.urls import reverse_lazy
from core.mixins import DashboardMixin
from django.utils import timezone
from datetime import date, datetime, timedelta
from core.models import Clinica,ListaEspera
from controle_usuarios.models import Profissional
from pacientes.models import Paciente
from django.contrib import messages
from core.forms import ListaEsperaForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from core.decorators import staff_member_required
from django.core.exceptions import ValidationError


class DashboardView(TemplateView,DashboardMixin):
    template_name = 'dashboard.html'

    def get_context_data(self, *args, **kwargs):
        create_clinic_when_init_system()
        context = super(DashboardView, self).get_context_data(*args, **kwargs)
        #contexto enviado para permmissoes de atendentee profissional
        """
        context['atendente'] = Profissional.objects.filter(
            user=self.request.user,tipo=1
        )
        """
        
        context['clinica']          = Clinica.objects.all()[:1]        
        return context


'''
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+                           CRUD Lista de Espera
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''
@login_required
def EsperaCreateView(request):
    form = ListaEsperaForm(request.POST or None)
    if form.is_valid():
        new                  = ListaEspera()
        new.criado_em        = form.cleaned_data.get('criado_em')
        new.nome             = form.cleaned_data.get('nome')
        new.telefone         = form.cleaned_data.get('telefone')
        new.especialidade    = form.cleaned_data.get('especialidade')
        new.observacao       = form.cleaned_data.get('observacao')
        new.urgente          = form.cleaned_data.get('urgente')
        lista = ListaEspera.objects.filter(nome=new.nome, especialidade=new.especialidade).exists()
        if lista:
            messages.error(request,'Erro: Paciente Já Existente na Base de Dados! ')
            return redirect('add_lista')
        else:
            new.save()
        messages.success(request,'Paciente adicionado com sucesso! ')
        return redirect('lista_espera')
    return render(request,'lista_de_espera/adicionar.html',{'form':form})    

class EsperaListView(LoginRequiredMixin,ListView,DashboardMixin):
    model         = ListaEspera
    context_object_name = 'lista'
    template_name = 'lista_de_espera/lista.html'
    paginate_by = 50
    
    def get_queryset(self, **kwargs):
        queryset = ListaEspera.objects.all()
        if self.request.GET.get('paciente'):
            paciente_search = self.request.GET.get('paciente')
            queryset = ListaEspera.objects.filter(
                nome__icontains=paciente_search).order_by('id')
        return queryset

class EsperaUpdateView(LoginRequiredMixin,UpdateView):
    model         = ListaEspera
    template_name = 'lista_de_espera/adicionar.html'
    form_class    = ListaEsperaForm
    success_url   = reverse_lazy('lista_espera')


class EsperaDetailView(LoginRequiredMixin,DetailView):
    model = ListaEspera
    template_name = 'lista_de_espera/lista_detalhe.html'
    context_object_name = 'espera'


class EsperaDeleteView(LoginRequiredMixin,DeleteView):
    model         = ListaEspera
    success_url   = reverse_lazy('lista_espera')
    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

@login_required
def load_profissional(request):
    especialidade_id = request.GET.get('especialidade')
    pf            = Profissional.prof_objects.filter(area_atuacao=especialidade_id)
    context = {
        'profissionais': pf
    }
    return render(request, 'lista_de_espera/profissionais.html',context)
    
'''
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+                           Aniversariantes
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''

@login_required
def aniversarios(request):
    today     = timezone.now().date()
    paciente  = Paciente.objects.filter(data_nascimento__day=today.day,data_nascimento__month=today.month)
    if  request.GET.get('date_ranger'):
        date_range        = request.GET.get('date_ranger')
        paciente          = Paciente.objects.filter(
            data_nascimento__day=date_range.split('/')[0],data_nascimento__month=date_range.split('/')[1])
    context   = {
        'pacientes':paciente,
    }
    return render(request,'aniversariantes.html',context)

def create_clinic_when_init_system():
    #cria se não existir
    if(not Clinica.objects.filter(id=1).exists()):
        Clinica.objects.create(id=1,clinica='AltaClin')