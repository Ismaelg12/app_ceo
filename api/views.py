from django.shortcuts import render
from rest_framework import generics
from pacientes.models import Paciente
from .serializers import PacienteSerializer
from rest_framework import views
from rest_framework.response import Response

class TotalList(views.APIView):

    def get(self, request):
        data = [
        	{
	        	"nome": Paciente.objects.all(), 
            }
        ]
        results = PacienteSerializer(data, many=True).data
        return Response(results)



