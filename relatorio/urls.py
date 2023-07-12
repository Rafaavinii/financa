from django.urls import path
from .views import *


urlpatterns = [
    path('porcategoria/', DespesaPorCategoriaAPIView.as_view(), name='despesaporcategoria'),
    path('pormes/', DespesaPorMesAPIView.as_view(), name='despesapormes')
]