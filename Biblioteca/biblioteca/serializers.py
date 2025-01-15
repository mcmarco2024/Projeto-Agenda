from rest_framework import serializers
from .models import Livro
rom rest_framework import serializers
from .models import Usuários
rom rest_framework import serializers
from .models import Emprestimo

class LivroSerializer(serializers.ModelSerializer):
class Meta:
    model = Livro
    fields = '__all__'

class UsuárioSerializer(serializers.ModelSerializer):
class Meta:
    model = Usuário
    fields = '__all__'

class EmprestimoSerializer(serializers.ModelSerializer):
    model = Emprestimo
    fields = '__all__'


    


