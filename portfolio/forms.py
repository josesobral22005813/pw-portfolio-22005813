from django import forms
from django.forms import ModelForm
from .models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'descrição da tarefa...'}),
            'prioridade': forms.NumberInput(attrs={'class': 'form-control', 'max': 3, 'min': 1}),
        }

        labels = {
            'titulo': 'Título',
            'concluido': 'Concluída',
        }

        help_texts = {
            'prioridade': 'prioridade: baixa=1, media=2, alta=3',
        }