# -*- coding: utf-8 -*-
from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import ListView,CreateView,TemplateView,UpdateView,DeleteView,DetailView
from django.urls import reverse_lazy
from core.mixins import DashboardMixin
from django.utils import timezone
from core.models import Clinica,ListaEspera
from controle_usuarios.models import Profissional
from pacientes.models import Paciente
from django.contrib import messages
from core.forms import ListaEsperaForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from core.decorators import staff_member_required


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
#view que migra o cadastro na lista de espera paera o cadastro de pacientes
def migrar_paciente(request,pk):
    lista_espera = ListaEspera.objects.get(pk=pk)
    Paciente.objects.create(  
        nome=lista_espera.nome,
        data_nascimento=lista_espera.data_nascimento,
        sexo=lista_espera.sexo,
        cpf=lista_espera.cpf,            
        sus=lista_espera.sus,             
        telefone=lista_espera.telefone,     
        telefone_fixo=lista_espera.telefone_fixo,  
        observacao=lista_espera.observacao,     
        tratamento='RE',    
    ).save()
    lista_espera.delete()
    messages.success(request,'Cadastro Migrado com Sucesso, Apenas Complete os dados ! ')
    return redirect('lista_espera')


class EsperaCreateView(LoginRequiredMixin,CreateView):
    model         = ListaEspera
    template_name = 'lista_de_espera/adicionar.html'
    form_class    = ListaEsperaForm
    success_url   = reverse_lazy('lista_espera')


class EsperaListView(LoginRequiredMixin,ListView):
    model         = ListaEspera
    context_object_name = 'lista'
    template_name = 'lista_de_espera/lista.html'
    
    # def get_context_data(self, **kwargs):
    #     #pf é querysets para exibir profissionais no template para o filtro
    #     pf            = Profissional.objects.filter(tipo=2,user=self.request.user,)
    #     context = super(EsperaListView, self).get_context_data(**kwargs)
    #     if pf.exists():
    #         context['lista'] = ListaEspera.objects.filter(profissional__user=self.request.user)
    #     else:
    #         context['lista'] = ListaEspera.objects.all()
    #     return context

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