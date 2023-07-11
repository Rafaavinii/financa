from .models import Despesa
from rest_framework import viewsets
from .serializers import DespesaSerializer
from rest_framework.permissions import IsAuthenticated

class DespesaViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Despesa.objects.all()
    serializer_class = DespesaSerializer