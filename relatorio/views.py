from rest_framework.views import APIView
from rest_framework.response import Response
from despesa.models import Despesa
from django.db.models import Sum

class DespesaPorCategoria(APIView):
    def get(self, request):
        
        usuario = request.user
        despesas = Despesa.objects.filter(usuario=usuario)
        valor_total = Despesa.objects.filter(usuario=usuario).aggregate(total=Sum('valor'))

        dado = {}
        
        for despesa in despesas:
            valor_percentual = (despesa.valor*100)/valor_total['total']

            if despesa.categoria in dado:
                dado[despesa.categoria] += round(valor_percentual, 2)
            else:
                dado[despesa.categoria] = round(valor_percentual, 2)
    
        
        return Response(dado, status=200)
