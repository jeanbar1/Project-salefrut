from django import forms
from .models import Produto

class ProdutoForms(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'
        widgets = {
            'nomeProd': forms.TextInput(attrs={'class': 'form-control'}),
            'tipoProd': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 11}),
            'origemProd': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 11}),
            'quantidadeProd': forms.NumberInput(attrs={'class': 'form-control'}),
        }
