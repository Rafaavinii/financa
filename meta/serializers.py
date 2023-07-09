from rest_framework import serializers

from meta.models import Meta

class MetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meta
        fields = '__all__'