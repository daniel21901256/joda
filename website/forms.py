from django import forms
from django.forms import ModelForm
from .models import *


class contactoForm(ModelForm):
    class Meta:
        model = contacto
        fields = '__all__'
    # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Insira o seu nome'}),
            'apelido': forms.TextInput(attrs={'placeholder': 'Insira o seu apelido'}),
            'telefone': forms.TextInput(attrs={'placeholder': 'Insira o seu contacto'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Ex: joda@gmail.com'}),
            'dataNasc': forms.NumberInput(attrs={'type': 'date'}),
        }

class quizzForm(ModelForm):
    class Meta:
        model = quizz
        fields = '__all__'
    # inserção de classes CSS para formatação de cada campo do formulário
        labels = {
            'pergunta_1': '1. Quantas receitas de carne exitem no nosso website?',
            'pergunta_2': '2. Quantas receitas de peixe exitem no nosso website?',
            'pergunta_3': '3. Quantas receitas de veggie exitem no nosso website?',
            'pergunta_4': '4. Quantas receitas de doces exitem no nosso website?',
            'pergunta_5': '5. Choco frito é um prato famoso de que região?',
            'pergunta_6': '6. Em 2020 q restaurante recebeu uma estrela Michelin?',
            'pergunta_7': '7. As migas é um prato famoso de que região?',
            'pergunta_8': '8. Quantas estrelas michelins têm o Chef Pedro Lemos?',
            'pergunta_9': '9. Quantas estrelas michelins têm o Chef José Avillez?',
            'pergunta_10': '10. Quantas estrelas michelins têm o Chef Ricardo.C?',
        }




