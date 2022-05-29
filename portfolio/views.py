from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import PostForm
from .models import *
from .quizz import desenha_grafico_resultados


def home_page_view(request):
    return render(request, 'portfolio/home.html')


def mim_page_view(request):
    return render(request, 'portfolio/mim.html')


def educacao_page_view(request):
    context = {
        "cadeiras": Cadeira.objects.all()
    }
    return render(request, 'portfolio/educacao.html', context)


def competencias_page_view(request):
    context = {
        "competencias": Competencia.objects.all()
    }
    return render(request, 'portfolio/competencias.html', context)


def projetos_page_view(request):
    context = {
        "projetos": Projeto.objects.all()
    }
    return render(request, 'portfolio/projetos.html', context)


def sobre_page_view(request):
    return render(request, 'portfolio/sobre.html')


def website_page_view(request):
    return render(request, 'portfolio/website.html')


def noticias_page_view(request):
    return render(request, 'portfolio/noticias.html')


def quizz_page_view(request):
    desenha_grafico_resultados(request)

    return render(request, 'portfolio/quizz.html')


def blog_page_view(request):
    context = {
        "posts": Post.objects.all()
    }
    return render(request, 'portfolio/blog.html', context)


def new_comment_view(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))

    context = {'form': form}

    return render(request, 'portfolio/new.html', context)


def edit_comment_view(request, comment_id):
    comment = Post.objects.get(id=comment_id)
    form = PostForm(request.POST or None, instance=comment)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))

    context = {'form': form, 'comment_id': comment_id}
    return render(request, 'portfolio/edit.html', context)


def delete_comment_view(request, comment_id):
    Post.objects.get(id=comment_id).delete()
    return HttpResponseRedirect(reverse('portfolio:blog'))