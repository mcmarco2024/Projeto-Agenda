from django.shortcuts import render
from rest_framework import viewsets
from .serializers import contatosSerializer
from .models import contatos 
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class contatosViewSet(viewsets.ModelViewSet):
    authenthication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = contatos.objects.all()
    serializer_class = contatosSerializer


