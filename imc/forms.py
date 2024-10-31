from django import forms

class ImcForms(forms.Form):
    peso = forms.CharField(
        label='Peso',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder': 'Digite sua altura'
            }
        ),
    )

    altura = forms.CharField(
        label = 'Altura',
        required=True,
        max_length=70,
        widget=forms.TextInput(
            attrs={
            'class':'form-control',
            'placeholder':'Digite seu Peso'
            }
        ),
    )

