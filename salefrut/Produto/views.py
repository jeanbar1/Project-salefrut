from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Produto  
from Produto.forms import ProdutoForms

#---------------Ler Produto----------------------
def lista_produto(request):
    produtos = Produto.objects.all()
    
    if request.GET:
        if request.GET.get('Nome do produto'):
            valorNome = request.GET.get('Nome do produto')
            produtos = produtos.filter(nomeProd__contains=valorNome)
        if request.GET.get('Tipo'):
            valorTipoProd = request.GET.get('Tipo')
            produtos = produtos.filter(tipoProd=valorTipoProd)
        if request.GET.get('Produtor'):
            valorOrigemProd = request.GET.get('Produtor')
            produtos = produtos.filter(origemProd__contains=valorOrigemProd)
        if request.GET.get('Quantidade caixa'):
            valorQuantidadeProd = request.GET.get('Quantidade caixa')
            produtos = produtos.filter(quantidadeProd=valorQuantidadeProd)

    return render(request, 'produto/lista.html', {'produtos': produtos})

#---------------Criar Produto------------------
def add_produto(request):
    if request.method == 'POST':
        form = ProdutoForms(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/produto/')
    else:
        form = ProdutoForms()
    return render(request, 'produto/add.html', {'form': form})

#---------------Atualizar Produto----------------
def edita_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    if request.method == 'POST':
        form = ProdutoForms(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/produto/')
    else:
        form = ProdutoForms(instance=produto)
    return render(request, "produto/edita.html", {'form': form})

#---------------Deletar Produto-------------------
def deleta_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    produto.delete()
    return HttpResponseRedirect('/produto/')

#------------Detalhe------------------------------
def detalhe(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    return render(request, 'produto/detalhe.html', {'produto': produto})
