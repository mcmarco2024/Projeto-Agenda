from rest_framework import serializers
from .models import contatos

class contatosSerializer(serializers.ModelSerializer):
    class Meta:
        model = contatos
        fields = '__all__'