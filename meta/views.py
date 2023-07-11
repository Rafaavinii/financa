from rest_framework import viewsets
from rest_framework import permissions
from meta.models import Meta
from meta.serializers import MetaSerializer

class MetaViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Meta.objects.all()
    serializer_class = MetaSerializer
