from django.urls import path
from .views import DespesaPorCategoria


urlpatterns = [
    path('', DespesaPorCategoria.as_view(), name='despesaporcategoria')
]