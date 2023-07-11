
from rest_framework import serializers
from .models import Receita

class ReceitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receita
        fields = '__all__'
        read_only_fields = ('usuario',)
    
    def create(self, validated_data):
        request = self.context['request']
        user = request.user
        receita = Receita.objects.create(usuario=user, **validated_data)

        return receita