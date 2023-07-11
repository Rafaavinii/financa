from rest_framework import serializers

from meta.models import Meta

class MetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meta
        fields = '__all__'
        read_only_fields = ('usuario',)
    
    def create(self, validated_data):
        request = self.context['request']
        user = request.user
        meta = Meta.objects.create(usuario=user, **validated_data)

        return meta