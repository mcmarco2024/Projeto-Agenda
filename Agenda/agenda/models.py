from django.db import models
class contatos (models.Model):
    nome = models.CharField(max_length = 50)
    telefone = models.CharField(max_length = 14)
    endereço = models.CharField(max_length = 30)
    email = models.CharField(max_length = 26)
    def __str__(self):
        return self.nome                                
