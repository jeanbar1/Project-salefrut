from django.db import models

class Produto(models.Model):
    nomeProd = models.CharField(max_length=200)
    tipoProd = models.CharField(max_length=200)
    origemProd = models.CharField(max_length=200)
    quantidadeProd = models.IntegerField()