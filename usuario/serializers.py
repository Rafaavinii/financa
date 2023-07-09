from rest_framework import serializers

from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from usuario.models import Usuario

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        
        return data

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'email']
    
    def create(self, validated_data):
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        email = validated_data['email']
        password = validated_data['password']

        usuario = Usuario.objects.create_user(first_name=first_name,last_name=last_name,username=email,email=email,password=password, valid_email=False)

        return usuario
