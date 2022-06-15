from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import PostForm
from .models import *
from .quizz import desenha_grafico_resultados
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


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

def apis_page_view(request):
    return render(request, 'portfolio/apis.html')


def sobre_page_view(request):
    return render(request, 'portfolio/sobre.html')


def website_page_view(request):
    return render(request, 'portfolio/website.html')


def noticias_page_view(request):
    context = {
        "noticias": Noticia.objects.all()
    }
    return render(request, 'portfolio/noticias.html', context)


def quizz_page_view(request):
    desenha_grafico_resultados(request)

    return render(request, 'portfolio/quizz.html')


def blog_page_view(request):
    context = {
        "posts": Post.objects.all()
    }
    return render(request, 'portfolio/blog.html', context)


def new_post_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('portfolio:login'))

    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))

    context = {'form': form}

    return render(request, 'portfolio/new.html', context)


def edit_post_view(request, post_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('portfolio:login'))

    post = Post.objects.get(id=post_id)
    form = PostForm(request.POST or None, instance=post)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))

    context = {'form': form, 'comment_id': post_id}
    return render(request, 'portfolio/edit.html', context)


def delete_post_view(request, post_id):
    Post.objects.get(id=post_id).delete()
    return HttpResponseRedirect(reverse('portfolio:blog'))


def view_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('portfolio:home'))
        else:
            return render(request, 'portfolio/login.html', {
                'message': 'Credenciais invalidas.'
            })

    return render(request, 'portfolio/login.html')


def view_logout(request):
    logout(request)

    return render(request, 'portfolio/login.html')
