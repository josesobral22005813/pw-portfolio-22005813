from django import forms
from django.forms import ModelForm
from .models import *


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


class ProjectForm(ModelForm):
    class Meta:
        model = Projeto
        fields = '__all__'

        widgets = {
            'titulo': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Introduza o titulo do seu projeto'}),
            'descricao': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Introduza a descricao do seu projeto'}),
            'imagem': forms.FileInput(attrs={'class': 'form-control'}),
            'ano': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Introduza o ano do seu projeto'}),
            'link': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Introduza o link do seu projeto'}),
            'tecnologias': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Introduza as tecnologias do seu projeto'}),
        }

        labels = {
            'titulo': 'Titulo',
            'descricao': 'Descrição',
            'imagem': 'Imagem',
            'ano': 'Ano',
            'link': 'Link',
            'tecnologias': 'Tecnologias',
        }

        help_texts = {
        }


class CadeiraForm(ModelForm):
    class Meta:
        model = Cadeira
        fields = '__all__'

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Introduza o nome da cadeira'}),
            'ano': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Introduza o ano da cadeira'}),
            'semestre': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Introduza o semestre da cadeira'}),
            'descricao': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Introduza os ects da cadeira'}),
            'ranking': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Introduza o ranking da cadeira'}),
            'link': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Introduza o link da cadeira'}),
        }

        labels = {
            'nome': 'Nome',
            'ano': 'Ano',
            'semestre': 'Semestre',
            'descricao': 'Descrição',
            'ranking': 'Ranking',
            'link': 'Link',
        }

        help_texts = {
        }
