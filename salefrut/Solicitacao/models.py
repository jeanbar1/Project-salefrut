from django.db import models

from salefrut import Produto, Usuario

class Solicitacao(models.Model):
    # ForengnKey: chave estrangeira de produto
    # on_delete=models.CASCADE: se o produto for excluido as  todas as solicitações associadas a esse produto também sejam excluídas automaticamente
    # related_name='solicitacoes: permite acessar todas as solicitações feitas por um usuário usando     "usuario.solicitacoes.all()."
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    solicitante = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='solicitacoes')
    data_solicitacao = models.DateTimeField(auto_now_add=True)
    quantidade = models.IntegerField()