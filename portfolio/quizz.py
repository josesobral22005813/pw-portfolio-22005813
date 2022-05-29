import matplotlib.pyplot as graph
from .models import PontuacaoQuizz


def desenha_grafico_resultados(request):
    if request.method == 'POST':
        quizz(request)
        entradas = PontuacaoQuizz.objects.all()
        entradasOrd = sorted(entradas, key=lambda item: item.pontuacao, reverse=False)

        autores = []
        pontuacoes = []

        for entrada in entradasOrd:
            autores.append(entrada.nome)
            pontuacoes.append(entrada.pontuacao)

        graph.figure(figsize=(13, 5), facecolor='#F8F4E3')
        graph.barh(autores, pontuacoes, color='#FFA185')
        graph.title("Todas as entradas!")
        graph.ylabel("Autores")
        graph.xlabel("Pontuações")

        graph.savefig('portfolio/static/portfolio/images/graph.png')


def quizz(request):
    n = request.POST['nome']
    p = pontuacao_quizz(request)
    r = PontuacaoQuizz(nome=n, pontuacao=p)
    r.save()


def pontuacao_quizz(request):
    pontuacao = 0

    q1 = request.POST['q1']
    if q1.lower() == "css":
        pontuacao += 5

    if request.POST['q2'].lower() == "django":
        pontuacao += 5

    if request.POST['q3'].lower() == "javascript":
        pontuacao += 5

    if request.POST['q4'].lower() == "v":
        pontuacao += 5

    return pontuacao
