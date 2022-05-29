from django import forms
from django.forms import ModelForm
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

        widgets = {
            'autor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Introduza o seu nome'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Introduza um titulo'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Introduza uma descrição'}),
        }

        labels = {
            'autor': 'Autor',
            'titulo': 'Título',
            'descricao': 'Descrição',
        }

        help_texts = {
        }