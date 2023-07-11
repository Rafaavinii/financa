from datetime import date
from rest_framework import serializers
from .models import Despesa

class DespesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Despesa
        fields = '__all__'
        read_only_fields = ('usuario',)
    
    def create(self, validated_data):
        request = self.context['request']
        user = request.user
        despesa = Despesa.objects.create(usuario=user, **validated_data)

        return despesa