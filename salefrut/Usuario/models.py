from django.db import models

class usuario(models.Model):
    nome = models.CharField(max_length=200)
    cpf = models.IntegerField()
    telefone = models.IntegerField()
    endereco = models.CharField(max_length=300)
    
    
class vendedor(usuario):
    descricao = models.CharField(max_length=300)
    
    