from rest_framework.views import APIView
from rest_framework.response import Response
from despesa.models import Despesa
from django.db.models import Sum
from datetime import datetime

class DespesaPorCategoriaAPIView(APIView):
    def get(self, request):
        
        usuario = request.user
        despesas = Despesa.objects.filter(usuario=usuario)
        valor_total = despesas.aggregate(total=Sum('valor'))

        dado = {}
        
        for despesa in despesas:
            valor_percentual = round((despesa.valor*100)/valor_total['total'], 2)

            if despesa.categoria in dado:
                dado[despesa.categoria] += valor_percentual
            else:
                dado[despesa.categoria] = valor_percentual
    
        
        return Response(dado, status=200)

class DespesaPorMesAPIView(APIView):

    def get(self, request):
        
        usuario = request.user
        despesas = Despesa.objects.filter(usuario=usuario)

        dado = {}

        for despesa in despesas:
            mes = despesa.data.month
            if mes in dado:
                dado[mes] += despesa.valor
            else:
                dado[mes] = despesa.valor
        
        return Response(dado, status=200)
