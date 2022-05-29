from django import forms
from django.forms import ModelForm
from .models import Post


class CommentForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'descrição da tarefa...'}),
        }

        labels = {
            'titulo': 'Título',
        }

        help_texts = {
        }