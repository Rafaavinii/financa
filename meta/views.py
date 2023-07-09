from rest_framework import viewsets

from meta.models import Meta
from meta.serializers import MetaSerializer

class MetaViewset(viewsets.ModelViewSet):
    queryset = Meta.objects.all()
    serializer_class = MetaSerializer
