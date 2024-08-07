from django.shortcuts import get_object_or_404, redirect, render

from salefrut import Produto
from salefrut.Solicitacao.forms import SolicitacaoForm

# Create your views here.
def solicitar_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    if request.method == 'POST':
        form = SolicitacaoForm(request.POST)
        if form.is_valid():
            solicitacao = form.save(commit=False)
            solicitacao.produto = produto
            solicitacao.solicitante = request.user
            solicitacao.save()
            return redirect('lista_produtos')
    else:
        form = SolicitacaoForm()
    return render(request, 'marketplace/solicitar_produto.html', {'form': form, 'produto': produto})