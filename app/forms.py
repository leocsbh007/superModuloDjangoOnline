from django.forms import ModelForm
from .models import Produto
from django.core.exceptions import ValidationError


class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'marca','preco', 'estoque']
    
    def clean_nome(self):
        nome = self.cleaned_data.get('nome')

        if len(nome) < 3 or nome != '' or nome == ' ':
            raise ValidationError('Nome do Produto tem menos de 3 caracteres os esta em branco')
        
        return nome