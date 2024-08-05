from django.forms import ModelForm, TextInput
from .models import  vendedor

class vendedorForm(ModelForm):
    class Meta:
        model = vendedor
        fields = '__all__'
        widgets = {
            'nome': TextInput(attrs={'class': 'form-control'}),
            'cpf': TextInput(attrs={'class': 'form-control', 'maxlength': 11}),
            'telefone': TextInput(attrs={'class': 'form-control', 'maxlength': 11}),
            'endereco': TextInput(attrs={'class': 'from-control from-control-user'}),
            'descricao': TextInput(attrs={'class': 'form-control'}),
        }
