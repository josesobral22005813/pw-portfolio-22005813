from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=50)
    linkLusofona = models.TextField(blank=True)
    linkLinkedIn = models.TextField(blank=True)

    def __str__(self):
        return self.nome


class Competencia(models.Model):
    titulo = models.CharField(max_length=30)
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo


def resolution_path(instance, filename):
    return f'users/{instance.id}/'


class Projeto(models.Model):
    titulo = models.CharField(max_length=30)
    descricao = models.CharField(max_length=500)
    imagem = models.ImageField(upload_to=resolution_path)
    ano = models.IntegerField()
    participantes = models.ManyToManyField(Pessoa)
    gitLink = models.TextField()
    tecnologias = models.TextField()
    competencias = models.ManyToManyField(Competencia, blank=True)

    def __str__(self):
        return self.titulo


class Cadeira(models.Model):
    nome = models.CharField(max_length=50)
    ano = models.IntegerField()
    semestre = models.IntegerField()
    ects = models.IntegerField()
    descricao = models.TextField()
    ranking = models.IntegerField()
    professores = models.ManyToManyField(Pessoa)
    link = models.CharField(max_length=100)
    projetos = models.OneToOneField(Projeto, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nome


class Comment(models.Model):
    titulo = models.CharField(max_length=200)
    prioridade = models.IntegerField(default=1)
    concluido = models.BooleanField(default=False)
    criado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo[:50]


class PontuacaoQuizz(models.Model):
    nome = models.CharField(max_length=200)
    pontuacao = models.IntegerField()

    def __str__(self):
        return f"{self.nome}"