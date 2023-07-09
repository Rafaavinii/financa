from datetime import date
from rest_framework import serializers
from .models import Despesa

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Despesa
        fields = '__all__'
        read_only_fields = ('data', 'usuario',)
    
    def create(self, validated_data):
        request = self.context['request']
        user = request.user
        data_atual = date.today()
        despesa = Despesa.objects.create(data=data_atual, usuario=user, **validated_data)

        return despesa