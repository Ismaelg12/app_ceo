from django.urls import path
from core import views as v
from django.views.generic.base import TemplateView


urlpatterns = [
    path('dashboard/',v.DashboardView.as_view(),name='home'),
    path('aniversariantes/',v.aniversarios,name='aniversario'),
    ######################LISTA DE ESPERA############################################
	path('lista_espera/',v.EsperaListView.as_view(),name='lista_espera'),
	path('ajax/profissionais/', v.load_profissional, name='ajax_load_profissionais'),
	path('adicionar/lista_espera/',v.EsperaCreateView.as_view(),name='add_lista'),
	path('atualizar/lista_espera/<int:pk>/',v.EsperaUpdateView.as_view(),name='update_lista_espera'),
	path('lista_espera/<int:pk>/migrar_paciente/',v.migrar_paciente,name='migrar_paciente'),
	path('lista_espera/<int:pk>/detalhe/',v.EsperaDetailView.as_view(),name='lista_espera_detalhe'),
	path('deletar/lista_espera/<int:pk>/',v.EsperaDeleteView.as_view(),name='deletar_lista_espera'),
	####################################ACESSO NEGADO##########################################
	path('acesso/negado/',TemplateView.as_view(template_name="erros/403.html"),name='erro_403'),
]
