from django.urls import path
from .views import *

urlpatterns = [
    path('login/', CustomTokenObtainPairView.as_view(), name='token'),
    path('cadastro/', UsuarioViewSet.as_view(), name='cadastro')
]