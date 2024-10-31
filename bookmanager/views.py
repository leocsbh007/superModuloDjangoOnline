from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Livro
import datetime
import json


def index(request):
    now = datetime.datetime.now()
    html = "<html><body><h1>My Book Manager </h1></body></html>"
    return HttpResponse(html)

@csrf_exempt
@require_http_methods(['POST'])
def criar_livro(request):
    # Verifica se o corpo da requisição contem dados
    if not request.body:
        return JsonResponse({'error' : 'Dados Vazios'}, status=400)

    # Decodificar o JSON
    try:
        dados = json.loads(request.body)
    except json.JSONDecodeError as e:
        print('Erro ao decodificar JSON')
        return JsonResponse({'error':str(e), 'message' : 'Erro ao decodificar o JSON'}, status=400)

    # Validar campos obrigatorios
    required_fields = ['titulo', 'autor','data_publicacao','numero_paginas']
    for field in required_fields:
        if field not in dados:
            return JsonResponse({'error' : f'O campo {field} é obrigatorio'}, status=400)

    livro = Livro.objects.create(
        titulo = dados.get('titulo'),
        autor = dados.get('autor'),
        data_publicacao = dados.get('data_publicacao'),
        numero_paginas = dados.get('numero_paginas')
    )
    print(livro)
    return JsonResponse({'id':livro.id, 'message': 'Livro Adicionado com Sucesso!'}, status=201)

@csrf_exempt
@require_http_methods(['GET'])
def listar_livros(request):
    livros = Livro.objects.all().values()
    return JsonResponse(list(livros), safe=False)

@csrf_exempt
@require_http_methods(['PUT'])
def atualizar_livro(request, livro_id):
    try:
        # Tenta obter o livro com o ID fornecido
        livro = Livro.objects.get(id=livro_id)

        # Decodificar o JSON
        try:
            dados = json.loads(request.body)
        except json.JSONDecodeError as e:
            print('Erro ao decodificar JSON')
            return JsonResponse({'error':str(e), 'message' : 'Erro ao decodificar o JSON'}, status=400)
    
        # Atualiza os campos do livro 
        livro.titulo = dados.get('titulo')
        livro.autor = dados.get('autor')
        livro.data_publicacao = dados.get('data_publicacao')
        livro.numero_paginas = dados.get('numero_paginas')

        # Atualiza o Banco
        livro.save()
        print(livro)
        return JsonResponse({'message':'Livro atualizado com sucesso!!!'})

    # Se o id Fornecido não existir
    except: 
        return JsonResponse({'error': 'Produto não encontrado'}, status=404)