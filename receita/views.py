from .models import Receita
from rest_framework import viewsets
from .serializers import ReceitaSerializer
from rest_framework.permissions import IsAuthenticated

class ReceitaViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer