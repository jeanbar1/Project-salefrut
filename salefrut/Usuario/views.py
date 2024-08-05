from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import vendedor
from Usuario.form import vendedorForm


#---------------Ler Usuario----------------------
def lista_vendedor(request):
    vendedo = vendedor.objects.all()
    
    if request.GET:
        if request.GET.get('nome'):
            valorNome = request.GET.get('nome')
            vendedo = vendedo.filter(nome__contains = valorNome)
        if request.GET.get('cpf'):
            valorCpf = request.GET.get('cpf')
            vendedo = vendedo.filter(cpf__contains = valorCpf)
        if request.GET.get('telefone'):
            valorTelefone = request.GET.get('telefone')
            vendedo = vendedo.filter(telefone__contains = valorTelefone)
        if request.GET.get('endereco'):
            valorEndereco = request.GET.get('endereco')
            vendedo = vendedo.filter(endereco = valorEndereco)
        if request.GET.get('descricao'):
            valorDescricao = request.GET.get('descricao')
            vendedo = vendedo.filter(descricao = valorDescricao)
            
    else:
        vendedo = vendedor.objects.all()
    return render(request,  'vendedor/lista.html', {'vendedo': vendedo })

#---------------Criando usuario------------------
def add_Vendedor(request):
    if request.method == 'POST' :
        form = vendedorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/vendedor/')
    else:
        form = vendedorForm()
    return render(request, 'vendedor/add.html', {'form': form})

                
#---------------Atualizar usuario----------------
def edita_vendedor(request, vendedor_id):
    vendedores = vendedor.objects.get(id = vendedor_id)
    if request.method == 'POST' :
        form = vendedorForm(request.POST, instance= vendedores)
        if form.is_valid():
           form.save()
           return HttpResponseRedirect('/vendedor/')

    else:
        form = vendedorForm(instance = vendedores)        
    return render(request, "vendedor/edita.html", {'form': form})
#---------------Deleta usuario-------------------

def deleta_vendedor(request, vendedor_id):
    vendedor.objects.get(id = vendedor_id).delete()
    
    return HttpResponseRedirect('/vendedor/')


#------------detalhe------------------------------
def detalhe(request, vendedor_id):
    vendedores = vendedor.objects.get(id = vendedor_id)
    
    return render(request, 'vendedor/detalhe.html', {'vendedor' : vendedores})