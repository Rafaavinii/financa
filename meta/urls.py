from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter
from .views import MetaViewset

# Criar um roteador para o ViewSet
router = DefaultRouter()
router.register('', MetaViewset, basename='despesas')

urlpatterns = [
    # Adicionar as URLs do roteador ao urlpatterns
] + router.urls