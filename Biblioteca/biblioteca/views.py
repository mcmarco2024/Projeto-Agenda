from django.shortcuts import render

from rest_framework import viewsets
from .models import  Livro,Usuario, Emprestimo
from .serializers import AutorSerializer, CategoriaSerializer, LivroSerializer, EmprestimoSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import ISAuthenticated

class Livro_viewset(viewsets.ModelViewSet):
    authention_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = LivroSerializer.objects.all()
    serializer_class= Livro_Serializer   

class Usuario_viewset(viewsets.ModelViewSet):
    authention_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]    
    queryset = Usuario.objects.all()
    serializer_class = Usuario_Serializer 

class Emprestimo_viewset(viewsets.ModelViewSet):
    authention_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Emprestimo.objects.all()
    serializer_class = Emprestimo_Serializer


