from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter
from .views import DespesaViewset

# Criar um roteador para o ViewSet
router = DefaultRouter()
router.register('', DespesaViewset, basename='despesas')

urlpatterns = [
    # Adicionar as URLs do roteador ao urlpatterns
] + router.urls